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

    # If page has outgoing links, then transition_model should return a probability distribution that chooses
    # randomly among all pages linked to by page with probability damping_factor, and chooses randomly among
    # all pages in the corpus with probability 1 - damping_factor, divided equally among all pages in the corpus.
    if corpus[page]:
        page_prob = dict()
        for link in corpus:
            page_prob[link] = (1 - damping_factor) / len(corpus)
            if link in corpus[page]:
                page_prob[link] += damping_factor / len(corpus[page])
        return page_prob
    else:
        # If the page has no outgoing links, then choose randomly among all pages with equal probability.
        return {link: 1 / len(corpus) for link in corpus}


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_rank = dict()
    sample = None
    random.seed()

    # Initialize each page with a rank of 0
    for page in corpus:
        page_rank[page] = 0
    for _ in range(n):
        if sample is None:
            sample = random.choice(list(corpus.keys()))
        else:
            model = transition_model(corpus, sample, damping_factor)
            sample = random.choices(
                list(model.keys()), weights=list(model.values()), k=1
            )[0]
        page_rank[sample] += 1

    # Normalize the page ranks
    for page in page_rank:
        page_rank[page] /= n
    return page_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    page_rank = {}
    new_rank = {}

    # Assign each page a rank of 1 / N, where N is the total number of pages in the corpus.
    for page in corpus:
        page_rank[page] = 1 / len(corpus)

    repeat = True
    while repeat:
        for page in page_rank:
            total = 0

            for link in corpus:
                # If a page has links, then its PageRank should be divided evenly amongst all of its links.
                if page in corpus[link]:
                    total += page_rank[link] / len(corpus[link])
                # If a page has no links, then its PageRank should be evenly distributed amongst all pages
                # (including itself) with links.
                if not corpus[link]:
                    total += page_rank[link] / len(corpus)

            new_rank[page] = (1 - damping_factor) / len(corpus) + damping_factor * total

        repeat = False

        for page, rank in page_rank.items():
            if abs(new_rank[page] - rank) > 0.001:
                repeat = True
            page_rank[page] = new_rank[page]

    return page_rank


if __name__ == "__main__":
    main()
