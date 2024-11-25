import sys
from hashlib import sha1

from download_piece import decode_bencode, extract_info_hash, download_piece


def main():
    if len(sys.argv) != 3:
        print("Usage: python simple_bittorrent_client.py <torrent_file> <output_txt_file>")
        sys.exit(1)

    torrent_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(torrent_file, "rb") as f:
            torrent_data = f.read()

        # Decode the torrent file
        decoded_data = decode_bencode(torrent_data)[0]

        # Extract the info hash
        info_hash = sha1(extract_info_hash(torrent_data)).digest()

        # Download the first piece
        if download_piece(decoded_data, info_hash, piece_index=0, output_file=output_file):
            print(f"First piece downloaded successfully to {output_file}.")
        else:
            print("Failed to download the first piece.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
