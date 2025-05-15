import pandas as pd

def extract_chunk(input_csv, output_csv, num_rows=100000, chunk_size=50000):
    rows_written = 0
    first_chunk = True

    for chunk in pd.read_csv(input_csv, chunksize=chunk_size):
        if rows_written + len(chunk) > num_rows:
            chunk = chunk.iloc[:num_rows - rows_written]

        if first_chunk:
            chunk.to_csv(output_csv, index=False)
            first_chunk = False
        else:
            chunk.to_csv(output_csv, mode='a', index=False, header=False)

        rows_written += len(chunk)
        print(f"Written {rows_written} rows so far...")

        if rows_written >= num_rows:
            break

    print(f"Done. Extracted {rows_written} rows to {output_csv}.")

if __name__ == "__main__":
    NUM_ROW = 100000
    extract_chunk("jpss_master_matrix.tsv", f"jpss_master_matrix_{NUM_ROW}row.tsv", num_rows=NUM_ROW)
