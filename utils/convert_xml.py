#!/usr/bin/python3
# _*_ coding: utf-8

import argparse
from ConvertOdtByXML import (
    Odt,
    convert_ucs_to_unicode_by_font,
    convert_unicode_to_ucs
)


def create_parser():
    _parser = argparse.ArgumentParser()
    _parser.add_argument(
        'odt',
        nargs=1,
        metavar="ODT",
        help='ODT url',
    )
    _parser.add_argument(
        '-s', '--save_format',
        action='store_true',
        default=False,
        help='Сохранять форматирование',
    )
    _parser.add_argument(
        '-f', '--style_font',
        nargs=1,
        action="store",
        metavar="FONT",
        help='Шрифт для замены в стилях.',
    )
    group_url_parser_db = _parser.add_argument_group('convert', 'Конвертация')
    gr = group_url_parser_db.add_mutually_exclusive_group()
    gr.add_argument(
        '-p', '--to_unicode',
        action='store_true',
        default=False,
        help='Конвертация в Unicode (Ponomar)',
    )
    gr.add_argument(
        '-u', '--to_ucs',
        action='store_true',
        default=False,
        help='Конвертация в UCS',
    )
    return _parser


def args_hanlder():
    parser = create_parser()
    args = parser.parse_args()
    _odt = None
    odt_obj = None
    _save_format = False
    if args.odt:
        _odt = args.odt[0]
        odt_obj = Odt(_odt)
    if args.save_format:
        _save_format = True
    if args.to_unicode or args.to_ucs:
        _function = None
        _function_args = None
        _converter = None
        _font = None

        if args.to_unicode:
            _converter = convert_ucs_to_unicode_by_font
            _font = 'Ponomar Unicode'  # default
        elif args.to_ucs:
            _converter = convert_unicode_to_ucs
            _font = 'Triodion Ucs'  # default

        if args.style_font:
            _font = args.style_font[0]
        odt_obj.set_style_font(_font)

        if _converter:
            odt_obj.set_converter(_converter)

        if _save_format:
            odt_obj.convert_with_saving_format()
        else:
            odt_obj.convert_text_only()
    else:
        print('[!] Or -p or -u option expected!')


def main():
    args_hanlder()


if __name__ == '__main__':
    main()
