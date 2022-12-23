#!/usr/bin/env python3

"""
Quickly fetch your WiFi password and if needed, generate a QR code
of your WiFi to allow phones to easily connect

by Siddharth Dushantha
"""

import sys
import argparse

import utils

__version__ = "1.1.1"


def main() -> None:
    parser = argparse.ArgumentParser(usage="%(prog)s [options]")
    parser.add_argument("--show-qr", "-show",
                        action="store_true",
                        default=False,
                        help="Show a ASCII QR code onto the terminal/console")

    parser.add_argument("--save-qr", "-save",
                        metavar="PATH",
                        nargs="?",
                        const="STORE_LOCALLY",
                        help="Create the QR code and save it as an image")

    parser.add_argument("--ssid", "-s",
                        help="Specify a SSID that you have previously connected to")

    parser.add_argument('--list', "-l", 
                        action="store_true", 
                        default=False, 
                        help="Lists all stored network SSID")

    parser.add_argument("--version",
                        action="store_true",
                        help="Show version number")
    
    args = parser.parse_args()

    if args.version:
        print(__version__)
        sys.exit()

    if args.list:
        profiles = utils.get_profiles()
        wifi_dict = utils.generate_wifi_dict(profiles)
        utils.print_dict(wifi_dict)
        return

    ssid = utils.get_ssid() if args.ssid is None else args.ssid.split(',')
    wifi_dict = utils.generate_wifi_dict(ssid)

    if args.show_qr or args.save_qr:
        for key, value in wifi_dict.items():
            utils.generate_qr_code(ssid=key, password=value, path=args.save_qr, show_qr=args.show_qr)
        return

    utils.print_dict(wifi_dict)

if __name__ == "__main__":
    main()