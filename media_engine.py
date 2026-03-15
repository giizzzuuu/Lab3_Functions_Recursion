def monitor(func):
    """Decorator to log processing status."""
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper

def play_count_stream(limit):
    """Generator yielding squared even numbers up to the limit."""
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i ** 2

@monitor
def run_analytics(limit):
    """Aggregates data from the stream."""
    gen = play_count_stream(limit)
    counts = []
    for val in gen:
        counts.append(val)

    total_plays = sum(counts)
    num_records = len(counts)
    return total_plays, num_records, counts