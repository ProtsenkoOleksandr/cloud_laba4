import boto3
import os, csv, json, sys, pathlib

def main():
    with open(sys.argv[1]) as csv_file:
        content = json.load(csv_file)
        head_new_content = content[0].keys()

    with open(sys.argv[2], "w", newline="") as csv_file:
        list_write = csv.writer(csv_file)
        list_write.writerow(head_new_content)
        for info in content:
            var = (x for x in info.values())
            list_write.writerow(var)

    s3 = boto3.client("s3")
    tag_bucket = "lab2prots"
    argv2_name = sys.argv[2]
    path_file = os.path.join(pathlib.Path(__file__).parent.resolve(), sys.argv[2])
    response = s3.upload_file(path_file, tag_bucket, argv2_name)

if __name__ == "__main__":
    main()