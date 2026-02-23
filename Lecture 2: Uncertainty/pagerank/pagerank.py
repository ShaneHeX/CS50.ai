import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    out_links = corpus[page]
    all_pages = corpus.keys()
    pr = {}

    # page has no outgoing links,
    # so choose randomly from all pages with equal probability
    if not len(out_links):
        random_choose_all_pages_prob = 1 / len(all_pages)
        for p in all_pages:
            pr[p] = random_choose_all_pages_prob
        return pr
    
    # page has outgoing links
    random_choose_all_pages_prob = (1 - damping_factor) / len(all_pages)
    for p in all_pages:
        pr[p] = random_choose_all_pages_prob

    random_choose_outlink_prob = damping_factor / len(out_links)
    for link in out_links:
        pr[link] += random_choose_outlink_prob

    return pr


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    all_pages = corpus.keys()
    page_counts = {page: 0 for page in all_pages}
    current_page = random.choice(list(all_pages))

    for _ in range(n):
        page_counts[current_page] += 1
        model = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices(list(model.keys()), list(model.values())).pop()

    return {page: count / n for page, count in page_counts.items()}


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    all_pages = corpus.keys()
    pr = {page: 1 / len(all_pages) for page in all_pages}

    while True:
        new_pr = {}

        for p in all_pages:
            new_pr[p] = (1 - damping_factor) / len(all_pages)
            for i in all_pages:
                # page i has an outgoing link to page p
                if p in corpus[i]:
                    new_pr[p] += damping_factor * pr[i] / len(corpus[i])
                # page i has no outgoing links, so treat it as having one outgoing link to every page
                elif not len(corpus[i]):
                    new_pr[p] += damping_factor * pr[i] / len(all_pages)

        # check for convergence
        if all(abs(new_pr[p] - pr[p]) < 0.001 for p in all_pages):
            break
        pr = new_pr

    return pr


if __name__ == "__main__":
    main()
