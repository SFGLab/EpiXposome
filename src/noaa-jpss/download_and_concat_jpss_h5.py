import os
import shutil
from pathlib import Path
import xarray as xr
import boto3
import pandas as pd

def download_and_process_s3_files(
    s3_bucket: str,
    s3_prefix: str,
    local_tmp_dir: str,
    output_file: str,
    max_files: int = None
):
    os.makedirs(local_tmp_dir, exist_ok=True)
    s3 = boto3.client('s3')

    paginator = s3.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=s3_bucket, Prefix=s3_prefix)

    files_processed = 0
    first_chunk = True
    local_files = []

    print(f"Listing files from s3://{s3_bucket}/{s3_prefix} ...")

    for page in pages:
        for obj in page.get('Contents', []):
            if max_files is not None and files_processed >= max_files:
                print(f"Reached max_files limit of {max_files}. Stopping download.")
                break

            key = obj['Key']
            filename = os.path.basename(key)
            local_path = os.path.join(local_tmp_dir, filename)

            print(f"Downloading {key} ...")
            s3.download_file(s3_bucket, key, local_path)
            local_files.append(local_path)

            print(f"Opening {filename} with xarray...")
            try:
                ds = xr.open_dataset(local_path, engine='netcdf4')
                df = ds.to_dataframe().reset_index()

                if first_chunk:
                    df.to_csv(output_file, index=False)
                    first_chunk = False
                else:
                    df.to_csv(output_file, mode='a', index=False, header=False)

                ds.close()
                files_processed += 1
                print(f"Processed {files_processed} files so far.\n")
            except Exception as e:
                print(f"Failed to open {filename}: {e}")

        else:
            # continue outer loop if inner loop didn't break
            continue
        # inner loop broke, break outer too
        break

    print(f"Done downloading and processing {files_processed} files.")
    print(f"Combined CSV saved to {output_file}.")

    # cleanup downloaded files and folder
    print(f"Cleaning up local files...")
    for f in local_files:
        os.remove(f)
    shutil.rmtree(local_tmp_dir)
    print("Cleanup done.")

if __name__ == "__main__":
    download_and_process_s3_files(
        s3_bucket='noaa-jpss',
        s3_prefix='NOAA20/VIIRS/NOAA20_VIIRS_Aerosol_Optical_Depth_Gridded_Reprocessed/0.05_Degrees_Daily/2018/',
        local_tmp_dir='tmp_noaa_files',
        output_file='jpss_master_matrix.tsv',
        max_files=10  #set  `None` to process all files
    )
