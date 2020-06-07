from collections import defaultdict

def print_histogram_2d(counts):
    '''
    Prints a two-dimensional histogram.

    :param counts: Data to visualize. The data have to be as a dict of dicts - i.e. in this format:
        {
            'category1': {
                'group1': <count>
                'group2': <count>
                ...
            },
            'category2': {
                'group1': <count>
                'group2': <count>
                ...
            }
            ...
        }
    '''
    idx_min = None
    idx_max = None
    sum_per_group = defaultdict(int)

    for key, cat_counts in counts.items():
        if idx_min is None or key < idx_min:
            idx_min = key

        if idx_max is None or key > idx_max:
            idx_max = key

        for group_name, count in cat_counts.items():
            sum_per_group[group_name] += count

    max_freq = None
    for key, cat_counts in counts.items():
        for group_name, count in cat_counts.items():
            freq = count / sum_per_group[group_name]
            if max_freq is None or max_freq < freq:
                max_freq = freq

    for key in range(idx_min, idx_max + 1):
        print(f'category {key}:')

        for group_name, count in counts[key].items():
            freq = count / sum_per_group[group_name]
            stars = '*' * round(freq * 100 / max_freq)
            print(f'  {group_name:20s} ({freq * 100:6.3f}%): {stars}')

