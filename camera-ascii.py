import cv2
import os
import argparse


def start_feed(video_source):
    cap = cv2.VideoCapture(video_source)
    while(cv2.waitKey(23) & 0xFF != ord('q')):
        screen_height,  screen_width = os.popen('stty size', 'r').read().split()
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        reduced = cv2.resize(gray, (int(screen_width), int(screen_height)))
        converted = to_ascii(reduced)
        print_terminal(converted)
    cap.release()
    cv2.destroyAllWindows()

def row_to_ascii(row):
    ascii_order = (' ', '.', "'", ',', ':', ';', 'c', 'l', 'x', 'o', 'k', 'X', 'd', 'O', '0', 'K', 'N')
    return tuple(ascii_order [int(x/(255/16))] for x in row)[::-1]

def to_ascii(input_grays):
    return tuple(row_to_ascii(row) for row in input_grays)

def print_terminal(input_ascii_array):
    os.system("clear")
    print('\n'.join((''.join(row) for row in input_ascii_array)), end='')


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--source", help="video source")
    args = vars(ap.parse_args())
    if args.get('source'):
        video_source = args.get('source')
    else:
        video_source = 0
    start_feed(video_source)
