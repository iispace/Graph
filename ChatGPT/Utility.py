def ReadLastTotalTokensFromFile(log_file_path):
    import os

    if not(os.path.exists(log_file_path)):
        last_total_tokens = 0
    else:
        with open(log_file_path, 'r') as f:
            for line in (f.readlines()[-2:-1]):
                _, str_tokens = line.split()
                last_total_tokens = int(str_tokens) 

    return last_total_tokens 
