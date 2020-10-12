import requests
import argparse


def get_photos(token: str, album_id: str):
    response = requests.get(
        f'https://api.vk.com/method/photos.get?v=5.77&album_id={album_id}&access_token={token}')
    response_json = response.json()
    count = response_json['response']['count']
    for i in range(count):
        sizes = response_json['response']['items'][i]['sizes']
        photo_info = sizes[len(sizes) - 1]
        photo_name = photo_info["url"].split('/')[-1]
        photo = requests.get(f'{photo_info["url"]}')
        with open(photo_name, 'wb') as g:
            g.write(photo.content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', dest='access_token', type=str, help='token for connect', required=True)
    parser.add_argument('-a', dest='album_id', type=str, help='album name for download', required=True)
    args = parser.parse_args()
    get_photos(args.access_token, args.album_id)


if __name__ == '__main__':
    main()
