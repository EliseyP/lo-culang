# _*_ coding: utf-8

from Letters import *

# -------------------------------------
# set of dictionaries for Orthodox fonts
# this is short form - symbols are not matching with Ponomar Unicode
# (matching symbols not replaced).

# взята из font_table_orthodox_tt без строки 'І': unicCapitalUkrI
font_table_ucs = {
    '#': Zvatelce,
    '$': Zvatelce + Oxia,
    '%': Zvatelce + Varia,
    '&': Titlo,
    '+': v_under + Pokrytie,
    '0': unicSmallO + Oxia,
    '1': Oxia,
    '2': Varia,
    '3': Zvatelce,
    '4': Zvatelce + Oxia,
    '5': Zvatelce + Varia,
    '6': Kamora,
    '7': Titlo,
    '8': erok_comb,
    '9': unicSmallZhe + Titlo,
    '<': x_under,
    '=': n_under + Pokrytie,
    '>': r_under + Pokrytie,
    '?': ch_under + Pokrytie,
    '@': Varia,
    'A': unicSmallA + Varia,
    'B': unicSmallYat + Kamora,
    'C': s_under + Pokrytie,
    'D': unicSmallDe + s_under + Pokrytie,
    'E': unicSmallIe + Varia,
    'F': unicCapitalFita,
    'G': unicSmallGhe + Titlo,
    'H': unicSmallOmega + Oxia,
    'I': unicCapitalUkrI,
    'J': unicSmallUkrI + Varia,
    'K': unicCapitalIotifA + Zvatelce,
    'L': unicSmallEl + d_under,
    'M': unicCapitalIzhitsa + dbl_grave,  # unicCapitalIzhitsaDblGrave,
    'N': unicCapitalRoundOmega + Zvatelce,
    'O': unicCapitalRoundOmega,
    'P': unicCapitalPsi,
    'Q': unicCapitalOmegaTitled,
    'R': unicSmallEr + Titlo,
    'S': unicSmallLittleYus + Varia,
    'T': unicCapitalOt,
    'U': unicCapitalUk,
    'V': unicCapitalIzhitsa,
    'W': unicCapitalOmega,
    'X': unicCapitalKsi,
    'Y': unicSmallMonogrUk + Varia,
    'Z': unicCapitalLittleYus,
    '\\': Titlo,
    '^': Kamora,
    '_': erok_comb,
    'a': unicSmallA + Oxia,
    'b': o_under + Pokrytie,
    'c': s_under + Pokrytie,
    'd': d_under,
    'e': unicSmallIe + Oxia,
    'f': unicSmallFita,
    'g': g_under + Pokrytie,
    'h': unicSmallYeru + Oxia,
    'i': unicSmallUkrI,
    'j': unicSmallUkrI + Oxia,
    'k': unicSmallIotifA + Zvatelce,
    'l': unicSmallEl + Titlo,
    'm': unicSmallIzhitsa + dbl_grave,  # unicSmallIzhitsaDblGrave,
    'n': unicSmallRoundOmega + Zvatelce,
    'o': unicSmallRoundOmega,
    'p': unicSmallPsi,
    'q': unicSmallOmegaTitled,
    'r': unicSmallEr + s_under + Pokrytie,
    's': unicSmallLittleYus + Oxia,
    't': unicSmallOt,
    'u': unicSmallUk,
    'v': unicSmallIzhitsa,
    'w': unicSmallOmega,
    'x': unicSmallKsi,
    'y': unicSmallMonogrUk + Oxia,
    'z': unicSmallLittleYus,
    '{': unicSmallMonogrUk + Kamora,
    '|': unicSmallLittleYus + Zvatelce + Varia,
    '}': unicSmallI + Titlo,
    '~': Oxia,
    '¤': thousands,
    '¦': unicSmallHa + Titlo,
    '§': unicSmallChe + Titlo,
    '©': unicSmallEs + Titlo,
    '®': unicSmallEr + d_under,
    '°': kavyka,
    '±': unicSmallIotifA + Zvatelce + Varia,
    'µ': unicSmallU,
    'Ё': unicSmallYat + Varia,
    'Ђ': unicSmallIzhitsa + Oxia,
    'Ѓ': unicCapitalA + Zvatelce + Oxia,
    # зачем присутствует, если совпадает с Ponomar u406?
    # и в таблице caps этой строки нет
    # 'І': unicCapitalUkrI,  # без точек, разница с triodion - (там с точками) unicCapitalYi
    'Ї': unicCapitalUkrI + Zvatelce,
    'Ј': unicCapitalUkrI + Zvatelce + Oxia,
    'Љ': unicCapitalLittleYus + Zvatelce,
    'Њ': unicCapitalOmega + Zvatelce,
    'Ћ': unicCapitalIotifA + Zvatelce + Oxia,
    'Ќ': unicCapitalUk + Zvatelce + Oxia,
    'Ў': unicCapitalUk + Zvatelce,
    'Џ': unicCapitalRoundOmega + Zvatelce + Oxia,
    'Э': unicCapitalYat,
    'Я': unicCapitalIotifA,
    'э': unicSmallYat,
    'я': unicSmallIotifA,
    'ё': unicSmallYat + Oxia,
    'ђ': unicSmallIzhitsa + g_under + Pokrytie,
    'ѓ': unicSmallA + Zvatelce + Oxia,
    'і': unicSmallUkrI + Kendema,
    'ї': unicSmallUkrI + Zvatelce,
    'ј': unicSmallUkrI + Zvatelce + Oxia,
    'љ': unicSmallLittleYus + Zvatelce,
    'њ': unicSmallOmega + Zvatelce,
    'ћ': unicSmallIotifA + Zvatelce + Oxia,
    'ќ': unicSmallUk + Zvatelce + Oxia,
    'ў': unicSmallUk + Zvatelce,
    'џ': unicSmallRoundOmega + Zvatelce + Oxia,
    'Ґ': unicCapitalA + Zvatelce,
    'ґ': unicSmallA + Zvatelce,
    '†': unicSmallA + Kamora,
    '‡': unicSmallUkrI + Kamora,
    '•': zh_under,
    '…': unicSmallKsi + Titlo,
    '‰': unicSmallLittleYus + Kamora,
    '‹': unicSmallUkrI + Titlo,
    '›': unicSmallIzhitsa + Kamora,
    '€': z_under,
    '№': unicSmallA + Titlo,
    '™': unicSmallTe + Titlo,
    'У': unicCapitalMonogrUk,
    'у': unicSmallMonogrUk,
}
# взята из font_table_orthodox_tt_caps
font_table_usc_caps = {
    '#': Zvatelce,
    '$': Zvatelce + Oxia,
    '%': Zvatelce + Varia,
    '&': Titlo,
    '+': v_under + Pokrytie,
    '0': unicCapitalO + Oxia,
    '1': Oxia,
    '2': Varia,
    '3': Zvatelce,
    '4': Zvatelce + Oxia,
    '5': Zvatelce + Varia,
    '6': Kamora,
    '7': Titlo,
    '8': erok_comb,
    '9': unicCapitalZhe + Titlo,
    '<': x_under,
    '=': n_under + Pokrytie,
    '>': r_under + Pokrytie,
    '?': ch_under + Pokrytie,
    '@': Varia,
    'A': unicCapitalA + Varia,
    'B': unicCapitalYat + Kamora,
    'C': s_under + Pokrytie,
    'D': '\u0414' + s_under + Pokrytie,
    'E': unicCapitalIe + Varia,
    'F': unicCapitalFita,
    'G': '\u0413' + Titlo,
    'H': unicCapitalOmega + Oxia,
    'I': unicCapitalUkrI,
    'J': unicCapitalUkrI + Varia,
    'K': unicCapitalIotifA + Zvatelce,
    'L': '\u041B' + d_under,
    'M': unicCapitalIzhitsa + dbl_grave,  # unicCapitalIzhitsaDblGrave,
    'N': unicCapitalRoundOmega + Zvatelce,
    'O': unicCapitalRoundOmega,
    'P': unicCapitalPsi,
    'Q': unicCapitalOmegaTitled,
    'R': '\u0420' + Titlo,
    'S': unicCapitalLittleYus + Varia,
    'T': unicCapitalOt,
    'U': unicCapitalO + unicCapitalMonogrUk,
    'V': unicCapitalIzhitsa,
    'W': unicCapitalOmega,
    'X': unicCapitalKsi,
    'Y': unicCapitalMonogrUk + Varia,
    'Z': unicCapitalLittleYus,
    '\\': Titlo,
    '^': Kamora,
    '_': erok_comb,
    'a': unicCapitalA + Oxia,
    'b': o_under + Pokrytie,
    'c': s_under + Pokrytie,
    'd': d_under,
    'e': unicCapitalIe + Oxia,
    'f': unicCapitalFita,
    'g': g_under + Pokrytie,
    'h': '\u042B' + Oxia,
    'i': unicCapitalUkrI,
    'j': unicCapitalUkrI + Oxia,
    'k': unicCapitalIotifA + Zvatelce,
    'l': '\u041B' + Titlo,
    'm': unicCapitalIzhitsa + dbl_grave,  # unicCapitalIzhitsaDblGrave,
    'n': unicCapitalRoundOmega + Zvatelce,
    'o': unicCapitalRoundOmega,
    'p': unicCapitalPsi,
    'q': unicCapitalOmegaTitled,
    'r': '\u0420' + s_under + Pokrytie,
    's': unicCapitalLittleYus + Oxia,
    't': unicCapitalOt,
    'u': unicCapitalO + unicCapitalMonogrUk,
    'v': unicCapitalIzhitsa,
    'w': unicCapitalOmega,
    'x': unicCapitalKsi,
    'y': unicCapitalMonogrUk + Oxia,
    'z': unicCapitalLittleYus,
    '{': unicCapitalMonogrUk + Kamora,
    '|': unicCapitalLittleYus + Zvatelce + Varia,
    '}': unicCapitalI + Titlo,
    '~': Oxia,
    '¤': thousands,
    '¦': '\u0425' + Titlo,
    '§': '\u0427' + Titlo,
    '©': '\u0421' + Titlo,
    '®': '\u0420' + d_under,
    '°': kavyka,
    '±': unicCapitalIotifA + Zvatelce + Varia,
    'µ': unicCapitalMonogrUk,
    '¶': '\u00B6',
    '·': '\u00B7',
    '»': '\u00BB',
    'Ё': unicCapitalYat + Varia,
    'Ђ': unicCapitalIzhitsa + Oxia,
    'Ѓ': unicCapitalA + Zvatelce + Oxia,
    'Є': unicCapitalUkrIe,
    'Ї': unicCapitalUkrI + Zvatelce,
    'Ј': unicCapitalUkrI + Zvatelce + Oxia,
    'Љ': unicCapitalLittleYus + Zvatelce,
    'Њ': unicCapitalOmega + Zvatelce,
    'Ћ': unicCapitalIotifA + Zvatelce + Oxia,
    'Ќ': unicCapitalO + unicCapitalMonogrUk + Zvatelce + Oxia,
    'Ў': unicCapitalO + unicCapitalMonogrUk + Zvatelce,
    'Џ': unicCapitalRoundOmega + Zvatelce + Oxia,
    'У': unicCapitalMonogrUk,
    'Я': unicCapitalIotifA,
    'а': unicCapitalA,
    'б': '\u0411',
    'в': '\u0412',
    'г': '\u0413',
    'д': '\u0414',
    'е': unicCapitalIe,
    'ж': unicCapitalZhe,
    'з': '\u0417',
    'и': unicCapitalI,
    'й': '\u0419',
    'к': '\u041A',
    'л': '\u041B',
    'м': '\u041C',
    'н': '\u041D',
    'о': unicCapitalO,
    'п': '\u041F',
    'р': '\u0420',
    'с': '\u0421',
    'т': '\u0422',
    'у': unicCapitalMonogrUk,
    'ф': unicCapitalEf,
    'х': '\u0425',
    'ц': '\u0426',
    'ч': '\u0427',
    'ш': '\u0428',
    'щ': '\u0429',
    'ъ': '\u042A',
    'ы': '\u042B',
    'ь': '\u042C',
    'э': unicCapitalYat,
    'ю': '\u042E',
    'я': unicCapitalIotifA,
    'ё': unicCapitalYat + Oxia,
    'ђ': unicCapitalIzhitsa + g_under + Pokrytie,
    'ѓ': unicCapitalA + Zvatelce + Oxia,
    'є': unicCapitalUkrIe,
    'ѕ': '\u0405',
    'і': unicCapitalUkrI,
    'ї': unicCapitalUkrI + Zvatelce,
    'ј': unicCapitalUkrI + Zvatelce + Oxia,
    'љ': unicCapitalLittleYus + Zvatelce,
    'њ': unicCapitalOmega + Zvatelce,
    'ћ': unicCapitalIotifA + Zvatelce + Oxia,
    'ќ': unicCapitalO + unicCapitalMonogrUk + Zvatelce + Oxia,
    'ў': unicCapitalO + unicCapitalMonogrUk + Zvatelce,
    'џ': unicCapitalRoundOmega + Zvatelce + Oxia,
    'Ґ': unicCapitalA + Zvatelce,
    'ґ': unicCapitalA + Zvatelce,
    '†': unicCapitalA + Kamora,
    '‡': unicCapitalUkrI + Kamora,
    '•': zh_under,
    '…': unicCapitalKsi + Titlo,
    '‰': unicCapitalLittleYus + Kamora,
    '‹': unicCapitalUkrI + Titlo,
    '›': unicCapitalIzhitsa + Kamora,
    '€': z_under,
    '№': unicCapitalA + Titlo,
    "™": '\u0422' + Titlo,
}

font_table_orthodox_e_roos = {
    # '#': '\uD83D' + '\uDD44',
    '#': NotchedRightSemicircleWithThreeDots,  # 🕄
    # '$': '\uD83D' + '\uDD42',
    '$': CrossPommee,  # 🕂
    # '%': '\uD83D' + '\uDD41',
    '%': CrossPommeeWithHalfCircleBelow,  # 🕁
    '0': unicDigitZero,
    '1': unicDigitOne,
    '2': unicDigitTwo,
    '3': unicDigitThree,
    '4': unicDigitFour,
    '5': unicDigitFive,
    '6': unicDigitSix,
    '7': unicDigitSeven,
    '8': unicDigitEight,
    '9': unicDigitNine,
    # '@': '\uD83D' + '\uDD43',
    '@': NotchedLeftSemicircleWithThreeDots,  # 🕃
    'A': unicCapitalA + Oxia,
    'E': unicCapitalIe + Oxia,
    'I': unicCapitalUkrI,
    # 'M': '\uD83D' + '\uDD45',
    'M': SymbolForMarksChapter,  # 🕅
    'O': unicCapitalRoundOmega,
    'U': unicCapitalMonogrUk + Oxia,
    'V': unicCapitalIzhitsa + Oxia,
    'W': unicCapitalO + Oxia,
    'Y': '\u042B' + Oxia,
    # '^': '\uD83D' + '\uDD40',
    '^': CircledCrossPommee,  # 🕀
    'a': unicSmallA + Oxia,
    'e': unicSmallIe + Oxia,
    'i': unicSmallUkrI,
    'o': unicSmallRoundOmega,
    'u': unicSmallU + Oxia,
    'v': unicSmallIzhitsa + Oxia,
    'w': unicSmallO + Oxia,
    'y': unicSmallYeru + Oxia,
    'Ђ': unicCapitalYat + Oxia,
    'Є': '\uE1A5',
    'Ј': unicCapitalUkrI + Oxia,
    'Њ': Oxia,
    'Ћ': unicCapitalYat,
    'Ќ': unicCapitalFita,
    'Џ': unicCapitalIzhitsa,
    'ђ': unicSmallYat + Oxia,
    'і': unicSmallUkrIWithDot,
    'ј': unicSmallUkrI + Oxia,
    'њ': Oxia,
    'ћ': unicSmallYat,
    'ќ': unicSmallFita,
    'џ': unicSmallIzhitsa,
    '†': CrossOrthodox,
    '‡': Dagger,
    'У': unicCapitalMonogrUk,
    "Ў": unicCapitalMonogrUk + '\u0306',
}

font_table_orthodox_digits = {
    '!': NotchedLeftSemicircleWithThreeDots,
    '#': CrossPommee,
    '$': CrossPommeeWithHalfCircleBelow,
    '%': CircledCrossPommee,
    '+': Dagger,
    ',': '\u002C',
    '.': '\u002E',
    '0': thousands,
    '1': unicSmallA + '\u20DD',
    '2': unicSmallA + '\u0488',
    '3': unicSmallA + '\u0489',
    '4': unicSmallA + '\uA670',
    '5': unicSmallA + '\uA671',
    '6': unicSmallYeru + '\uA672',
    ';': '\u002E',
    '=': CrossOrthodox,
    '?': '\u003B',
    '@': NotchedLeftSemicircleWithThreeDots,
    'E': unicSmallUkrIe + Titlo,
    'F': unicSmallFita + Titlo,
    'J': unicSmallUkrI + Titlo,
    'K': unicSmallKsi + Titlo,
    'M': SymbolForMarksChapter,
    'O': unicSmallRoundOmega + Titlo,
    'P': unicSmallPsi + Titlo,
    'S': '\u0455' + Titlo,
    'T': unicSmallOt,
    'W': unicSmallOmega + Titlo,
    'e': unicSmallUkrIe,
    'f': unicSmallFita,
    'j': unicSmallUkrI,
    'k': unicSmallKsi,
    'o': unicSmallRoundOmega,
    'p': unicSmallPsi,
    's': '\u0455',
    't': unicSmallOt,
    'w': unicSmallOmega,
    ';': '\u002E',
    'А': unicSmallA + Titlo,
    'Б': '\u0431' + Titlo,
    'В': '\u0432' + Titlo,
    'Г': unicSmallGhe + Titlo,
    'Д': unicSmallDe + Titlo,
    'Е': unicSmallIe + Titlo,
    'Ж': unicSmallZhe + Titlo,
    'З': '\u0437' + Titlo,
    'И': unicSmallI + Titlo,
    'К': '\u043A' + Titlo,
    'Л': unicSmallEl + Titlo,
    'М': '\u043C' + Titlo,
    'Н': '\u043D' + Titlo,
    'О': unicSmallO + Titlo,
    'П': '\u043F' + Titlo,
    'Р': unicSmallEr + Titlo,
    'С': unicSmallEs + Titlo,
    'Т': unicSmallTe + Titlo,
    'У': unicSmallU + Titlo,
    'Ф': unicSmallEf + Titlo,
    'Х': unicSmallHa + Titlo,
    'Ц': '\u0446' + Titlo,
    'Ч': unicSmallChe + Titlo,
    'Ш': '\u0448' + Titlo,
    'Щ': '\u0449' + Titlo,
    'ё': unicSmallYat,
    '∙': '\u00B7',
}

font_table_orthodox_loose = {
    '!': Oxia,
    '"': Varia,
    '#': Zvatelce,
    '$': Zvatelce + Oxia,
    '%': Zvatelce + Oxia,
    '&': Kamora,
    "'": kavyka,
    '*': unicSmallUkrI + Zvatelce,
    '+': Titlo,
    '-': '\u005F',
    '0': '\u030F',
    '1': Oxia,
    '2': Varia,
    '3': Zvatelce,
    '4': Zvatelce + Oxia,
    '5': Zvatelce + Varia,
    '6': Kamora,
    '8': unicSmallMonogrUk + Oxia,
    '9': unicSmallMonogrUk + Varia,
    '<': unicCapitalYa,
    '=': Titlo,
    '>': unicSmallYA,
    '?': '\u0021',
    '@': Varia,
    'F': unicCapitalFita,
    'G': zh_under,
    'H': x_under,
    'I': unicCapitalUkrI,
    'J': unicSmallUkrI + Kamora,
    'K': unicCapitalKsi,
    'L': unicSmallYat + Varia,
    'O': unicSmallOmegaTitled,
    'P': unicCapitalPsi,
    'Q': unicCapitalO,
    'R': r_under + Pokrytie,
    'S': '\u0405',
    'T': unicCapitalOt,
    'U': '\uE3BE',
    'V': unicCapitalIzhitsa,
    'W': unicCapitalOmega,
    'Y': unicSmallU,
    'Z': '\u0302',
    '\\': unicSmallUkrI + Zvatelce + Oxia,
    '^': Zvatelce + Varia,
    '`': '\u2E2F',
    'b': '\u0304',
    'c': s_under + Pokrytie,
    'd': d_under,
    'e': unicSmallUkrIe,
    'f': unicSmallFita,
    'g': g_under + Pokrytie,
    'h': ch_under + Pokrytie,
    'i': '\u0457',
    'j': unicSmallUkrI,
    'k': unicSmallKsi,
    'l': unicSmallYat + Kamora,
    'o': unicCapitalRoundOmega,
    'p': unicSmallPsi,
    'q': o_under + Pokrytie,
    'r': unicSmallEr + Titlo,
    's': '\u0455',
    't': unicSmallOt,
    'u': unicCapitalUk,
    'v': unicSmallIzhitsa,
    'w': unicSmallOmega,
    'y': unicSmallMonogrUk + Kamora,
    '{': v_under + Pokrytie,
    '|': unicCapitalUkrI + Zvatelce + Oxia,
    '}': z_under,
    '~': '\u2E2F',
    '«': unicSmallUkrI + Oxia,
    'Ё': unicCapitalYat,
    'Ђ': unicSmallGhe + Titlo,
    'Ѓ': unicSmallEl + Titlo,
    'Љ': unicCapitalUk + Zvatelce + Oxia,
    'Њ': unicCapitalUk + Zvatelce + Varia,
    'Ћ': unicSmallRoundOmega + Zvatelce,
    'Ќ': unicSmallUk + Zvatelce + Varia,
    'Џ': unicSmallRoundOmega + Zvatelce + Oxia,
    'О': unicCapitalRoundOmega,
    'У': unicSmallUk,
    'Э': unicCapitalIotifA,
    'Я': unicCapitalYa,  # unicCapitalLittleYus,
    'у': unicSmallMonogrUk,
    'э': unicSmallIotifA,
    'я': unicSmallLittleYus,
    'ё': unicSmallYat,
    'ђ': unicSmallA + Zvatelce + Oxia,
    'ѓ': unicSmallHa + Titlo,
    'љ': unicSmallZhe + Titlo,
    'њ': unicSmallI + Titlo,
    '‘': unicCapitalRoundOmega + Zvatelce,
    '’': unicCapitalRoundOmega + Zvatelce + Oxia,
    '‚': unicSmallTe + Titlo,
    '„': unicSmallChe + Titlo,
    '†': unicSmallIzhitsa + Zvatelce,
    '‡': unicSmallIzhitsa + Zvatelce + Oxia,
    '…': unicSmallIzhitsa + Oxia,
    '‰': unicSmallUk + Zvatelce,
    '‹': unicSmallUk + Zvatelce + Oxia,
    '€': unicCapitalUk + Zvatelce,
    '№': Zvatelce,
    '™': unicSmallUkrI + Oxia,
}

font_table_hirmos_ponomar = {
    '0': unicDigitZero,
    '1': unicDigitOne,
    '2': unicDigitTwo,
    '3': unicDigitThree,
    '4': unicDigitFour,
    '5': unicDigitFive,
    '6': unicDigitSix,
    '7': unicDigitSeven,
    '8': unicDigitEight,
    '9': unicDigitNine,
    'Ў': '\uE3BF',
    'У': unicCapitalMonogrUk,
    '': '\uEF00',
    '': '\uEF01',
    '': '\uEF02',
    '': '\uEF03',
    '': '\uEF04',
    '': '\uEF05',
    '': '\uEF06',
    '': '\uEF07',
    '': '\uEF08',
    '': '\uEF09',
    '': '\uEF0A',
    '': '\uEF0B',
    '': '\uEF10',
    '': '\uEF11',
    '': '\uEF12',
    '': '\uEF13',
    '': '\uEF14',
    '': '\uEF15',
    '': '\uEF16',
    '': '\uEF17',
    '': '\uE5D0',
    '': '\uE5D1',
    '': '\uE5D2',
    '': '\uE5D3',
    '': ZvatelceUp,
    '': Iso,
    '': IsoUp,
    '': Apostrof,
    '': ApostrofUp,
    '': ApostrofGreat,
    '': '\uE016',
    # '': '\uDB80' + '\uDC23',
    '': '\U000F0023',
    # '': '\uDB80' + '\uDC30',
    '': '\U000F0030',
    '': '\uE0E2',
    '': '\uE0E4',
    '': '\uE0EC',
    '': '\uE0ED',
    '': '\uE612',
    '': '\uE714',
    '': '\uE800',
    '': '\uE92D',
    '': '\uE92E',
    '': '\uE8E5',
    '': '\uE901',
    '': '\uE903',
    '': '\uE904',
    '': '\uE928',
    '': unicSmallUkrIWithDot,
}

font_table_irmologion = {
    '#': thousands,
    '$': CircledCrossPommee,
    '%': NotationDoubleSlash,
    '&': CrossPommeeWithHalfCircleBelow,
    "'": Oxia,
    '0': unicDigitZero,
    '1': unicDigitOne,
    '2': unicDigitTwo,
    '3': unicDigitThree,
    '4': unicDigitFour,
    '5': unicDigitFive,
    '6': unicDigitSix,
    '7': unicDigitSeven,
    '8': unicDigitEight,
    '9': unicDigitNine,
    '<': NotchedLeftSemicircleWithThreeDots,
    '>': NotchedRightSemicircleWithThreeDots,
    '@': kavyka,
    'E': '\uE0E4',
    'F': unicCapitalFita,
    'I': unicCapitalUkrI,
    'J': '\u046A',
    'K': unicCapitalIotifLittleYus,
    'L': '\u046C',
    'O': unicCapitalRoundOmega,
    'P': unicCapitalPsi,
    'Q': unicCapitalOmegaTitled,
    'S': '\u0405',
    'T': unicCapitalOt,
    'U': unicCapitalUk,
    'V': unicCapitalIzhitsa,
    'W': unicCapitalOmega,
    'X': unicCapitalKsi,
    'Y': unicCapitalIzhitsa + dbl_grave,  # unicCapitalIzhitsaDblGrave,
    'Z': unicCapitalIotifA,
    'c': '\u1C83',
    'e': unicSmallUkrIe,
    'f': unicSmallFita,
    'g': unicSmallU,
    'i': unicSmallYi,
    'j': '\u046B',
    'k': unicSmallIotifLittleYus,
    'l': '\u046D',
    'm': '\uA641',
    'n': '\u0465',
    'o': unicSmallRoundOmega,
    'p': unicSmallPsi,
    'q': unicSmallOmegaTitled,
    'r': unicSmallUkrI,
    's': '\u0455',
    't': unicSmallOt,
    'u': unicSmallUk,
    'v': unicSmallIzhitsa,
    'w': unicSmallOmega,
    'x': unicSmallKsi,
    'y': unicSmallIzhitsa + dbl_grave,  # unicSmallIzhitsaDblGrave,
    'z': unicSmallIotifA,
    '~': '\u0027',
    '°': '\u00AB',
    '±': '\u00AC',
    'Ē': '\u00B7',
    'У': unicCapitalMonogrUk,
    'Э': unicCapitalYat,
    'Я': unicCapitalLittleYus,
    'у': unicSmallMonogrUk,
    'э': unicSmallYat,
    'я': unicSmallLittleYus,
    '‡': Dagger,
}

# экзотика

font_table_ustav = {
    '"': Oxia,
    '#': Zvatelce + Oxia,
    '$': '\u003B',
    '%': Zvatelce,
    '&': Zvatelce + Varia,
    "'": Oxia,
    '*': Zvatelce + Varia,
    '+': erok_comb,
    '/': Titlo,
    '0': unicDigitZero,
    '1': unicDigitOne,
    '2': unicDigitTwo,
    '3': unicDigitThree,
    '4': unicDigitFour,
    '5': unicDigitFive,
    '6': unicDigitSix,
    '7': unicDigitSeven,
    '8': unicDigitEight,
    '9': unicDigitNine,
    ':': '\u003A',
    ';': '\u003B',
    '<': '\u00AB',
    '=': erok_comb,
    '>': '\u00BB',
    '@': Zvatelce + Oxia,
    'A': unicCapitalIotifA,
    'B': unicCapitalUkrI,
    'C': s_under + Pokrytie,
    'D': d_under,
    'E': unicCapitalYat,
    'F': unicCapitalFita,
    'G': g_under + Pokrytie,
    'H': unicCapitalIzhitsa + dbl_grave,  # unicCapitalIzhitsaDblGrave,
    'I': unicCapitalYi,
    'J': unicCapitalRoundOmega,
    'K': unicCapitalKsi,
    'L': kavyka,
    'M': Oxia,
    'N': unicCapitalOt,
    'O': o_under + Pokrytie,
    'P': unicCapitalPsi,
    'Q': unicCapitalOmegaTitled,
    'R': Pokrytie,
    'S': '\u0405',
    'T': '\u0465',
    'U': unicSmallMonogrUk,
    'V': unicCapitalIzhitsa,
    'W': unicCapitalOmega,
    'X': ch_under + Pokrytie,
    'Y': unicCapitalUk,
    'Z': unicCapitalYa,
    '\\': Titlo,
    '^': Zvatelce,
    '`': Varia,
    'a': unicSmallIotifA,
    'b': unicSmallUkrI,
    'c': s_under + Pokrytie,
    'd': d_under,
    'e': unicSmallYat,
    'f': unicSmallFita,
    'g': g_under + Pokrytie,
    'h': unicSmallIzhitsa + dbl_grave,  # unicSmallIzhitsaDblGrave,
    'i': unicSmallUkrI + Kendema,
    'j': unicSmallRoundOmega,
    'k': unicSmallKsi,
    'l': '\u1C82',
    'm': Oxia,
    'n': unicSmallOt,
    'o': o_under + Pokrytie,
    'p': unicSmallPsi,
    'q': unicSmallOmegaTitled,
    'r': Pokrytie,
    's': '\u0455',
    't': unicSmallUkrIe,
    'u': unicSmallMonogrUk,
    'v': unicSmallIzhitsa,
    'w': unicSmallOmega,
    'x': Varia,
    'y': unicSmallUk,
    'z': unicSmallYA,
    '{': Kamora,
    '|': Titlo,
    '}': Kamora,
    '~': Varia,
    '': unicCapitalIotifLittleYus,
    '': unicCapitalYa,
    '': '\u046B',
    '': ch_under + Pokrytie,
    '': unicCapitalFita,
    '': unicSmallIotifLittleYus,
    '': '\u040B',
    '': '\u1C82',
    '¡': unicCapitalUk,
    '¢': unicSmallUk,
    '£': unicCapitalIzhitsa + dbl_grave,  # unicCapitalIzhitsaDblGrave,
    '¥': unicCapitalOt,
    '¨': Varia,
    'ª': kavyka,
    '¯': unicCapitalYi,
    '²': unicCapitalUkrI,
    '³': unicSmallUkrI,
    '´': unicSmallOt,
    'µ': unicSmallMonogrUk + Varia,
    '¸': unicSmallIotifA,
    '¹': thousands,
    'º': unicSmallUkrIe,
    '¼': unicSmallIzhitsa + dbl_grave,  # unicSmallIzhitsaDblGrave,
    '½': '\u0405',
    '¾': '\u0455',
    '¿': '\u0457',
    'À': unicCapitalA,
    'Á': '\u0411',
    'Â': '\u0412',
    'Ã': '\u0413',
    'Ä': '\u0414',
    'Å': unicCapitalIe,
    'Æ': unicCapitalZhe,
    'Ç': '\u0417',
    'È': unicCapitalI,
    'É': '\u0419',
    'Ê': '\u041A',
    'Ë': '\u041B',
    'Ì': '\u041C',
    'Í': '\u041D',
    'Î': unicCapitalO,
    'Ï': '\u041F',
    'Ð': '\u0420',
    'Ñ': '\u0421',
    'Ò': '\u0422',
    'Ó': unicCapitalMonogrUk,
    'Ô': unicCapitalEf,
    'Õ': '\u0425',
    'Ö': '\u0426',
    '×': '\u0427',
    'Ø': '\u0428',
    'Ù': '\u0429',
    'Ú': '\u042A',
    'Û': '\u042B',
    'Ü': '\u042C',
    'Ý': '\u042D',
    'Þ': '\u042E',
    'ß': unicCapitalLittleYus,
    'à': unicSmallA,
    'á': '\u0431',
    'â': '\u0432',
    'ã': unicSmallGhe,
    'ä': unicSmallDe,
    'å': unicSmallIe,
    'æ': unicSmallZhe,
    'ç': '\u0437',
    'è': unicSmallI,
    'é': '\u0439',
    'ê': '\u043A',
    'ë': unicSmallEl,
    'ì': '\u043C',
    'í': '\u043D',
    'î': unicSmallO,
    'ï': '\u043F',
    'ð': unicSmallEr,
    'ñ': unicSmallEs,
    'ò': unicSmallTe,
    'ó': unicSmallU,
    'ô': unicSmallEf,
    'õ': unicSmallHa,
    'ö': '\u0446',
    '÷': unicSmallChe,
    'ø': '\u0448',
    'ù': '\u0449',
    'ú': '\u044A',
    'û': unicSmallYeru,
    'ü': '\u044C',
    'ý': '\u044D',
    'þ': '\u044E',
    'ÿ': unicSmallLittleYus,
    'Œ': unicSmallU,
    'œ': '\u045B',
    'Š': unicCapitalPsi,
    'š': '\u046D',
    'Ÿ': unicCapitalUkrI,
    'ƒ': unicCapitalYa,
    '˜': '\u2053',
    'Ё': Varia,
    'Ђ': unicCapitalIotifLittleYus,
    'Ѓ': unicCapitalYa,
    'Є': kavyka,
    'Ѕ': '\u0405',
    'Ј': unicCapitalIzhitsa + dbl_grave,  # unicCapitalIzhitsaDblGrave,
    'Ћ': ch_under + Pokrytie,
    'Ќ': '\u046B',
    'Ў': unicCapitalUk,
    'Џ': unicCapitalFita,
    'Я': unicCapitalLittleYus,
    'я': unicSmallLittleYus,
    'ё': unicSmallIotifA,
    'ђ': unicSmallIotifLittleYus,
    'ј': unicSmallIzhitsa + dbl_grave,  # unicSmallIzhitsaDblGrave,
    'ћ': '\u1C82',
    'ќ': '\u040B',
    'ў': unicSmallUk,
    'Ґ': unicCapitalOt,
    'ґ': unicSmallOt,
    '‘': Oxia,
    '’': Oxia,
    '‚': '\u002C',
    '“': Oxia,
    '”': Oxia,
    '‡': CrossOrthodox,
    '№': thousands,
    '™': '\u002A',
    'У': unicCapitalMonogrUk,
}

font_table_valaam = {
    '"': '\u030F',
    '#': thousands,
    '$': '\u003B',
    '%': Zvatelce,
    '&': Zvatelce,
    "'": Oxia,
    '*': '\u002A',
    '+': erok_comb,
    '/': Oxia,
    '0': unicDigitZero,
    '1': unicDigitOne,
    '2': unicDigitTwo,
    '3': unicDigitThree,
    '4': unicDigitFour,
    '5': unicDigitFive,
    '6': unicDigitSix,
    '7': unicDigitSeven,
    '8': unicDigitEight,
    '9': unicDigitNine,
    '<': '\u00AB',
    '=': kavyka,
    '>': '\u00BB',
    '@': Zvatelce + Oxia,
    'A': unicCapitalIotifLittleYus,
    'B': unicCapitalUkrI,
    'C': s_under + Pokrytie,
    'D': d_under,
    'E': unicCapitalYat,
    'F': unicCapitalFita,
    'G': g_under + Pokrytie,
    'H': '\u040B',
    'I': unicCapitalUkrI,
    'J': unicCapitalRoundOmega + Zvatelce,
    'K': unicCapitalKsi,
    'L': Zvatelce + Varia,
    'M': Zvatelce + Varia,
    'N': o_under + Pokrytie,
    'O': unicCapitalOt,
    'P': unicCapitalPsi,
    'Q': unicCapitalBroadOmega,
    'R': Pokrytie,
    'S': '\u0405',
    'T': '\u0465',
    'U': unicSmallMonogrUk,
    'V': unicCapitalIzhitsa,
    'W': unicCapitalOmega,
    'X': Zvatelce + Oxia,
    'Y': unicCapitalUk,
    'Z': unicCapitalIotifA,
    '\\': Varia,
    '^': Pokrytie,
    '_': '\u2014',
    '`': Varia,
    'a': unicSmallIotifLittleYus,
    'b': '\u046D',
    'c': s_under + Pokrytie,
    'd': d_under,
    'e': unicSmallYat,
    'f': unicSmallFita,
    'g': g_under + Pokrytie,
    'h': '\u045B',
    'i': '\u0457',
    'j': unicSmallRoundOmega + Zvatelce,
    'k': unicSmallKsi,
    'l': Zvatelce + Varia,
    'm': Zvatelce + Varia,
    'n': o_under + Pokrytie,
    'o': unicSmallOt,
    'p': unicSmallPsi,
    'q': unicSmallUkrI,
    'r': '\u046B',
    's': '\u0455',
    't': unicSmallIe,
    'u': unicSmallMonogrUk,
    'v': unicSmallIzhitsa,
    'w': unicSmallOmega,
    'x': Zvatelce + Oxia,
    'y': unicSmallUk,
    'z': unicSmallIotifA,
    '|': Kamora,
    '~': Titlo,
    '': ch_under + Pokrytie,
    '¨': Titlo,
    '´': unicCapitalMonogrUk,
    'µ': '\u2DE8',
    '¸': erok_comb,
    '¹': '\u2116',
    'À': unicCapitalA,
    'Á': '\u0411',
    'Â': '\u0412',
    'Ã': '\u0413',
    'Ä': '\u0414',
    'Å': unicCapitalIe,
    'Æ': unicCapitalZhe,
    'Ç': '\u0417',
    'È': unicCapitalI,
    'É': '\u0419',
    'Ê': '\u041A',
    'Ë': '\u041B',
    'Ì': '\u041C',
    'Í': '\u041D',
    'Î': unicCapitalO,
    'Ï': '\u041F',
    'Ð': '\u0420',
    'Ñ': '\u0421',
    'Ò': '\u0422',
    'Ó': unicCapitalMonogrUk,
    'Ô': unicCapitalEf,
    'Õ': '\u0425',
    'Ö': '\u0426',
    '×': '\u0427',
    'Ø': '\u0428',
    'Ù': '\u0429',
    'Ú': '\u042A',
    'Û': '\u042B',
    'Ü': '\u042C',
    'Ý': '\u042D',
    'Þ': '\u042E',
    'ß': unicCapitalLittleYus,
    'à': unicSmallA,
    'á': '\u0431',
    'â': '\u0432',
    'ã': unicSmallGhe,
    'ä': unicSmallDe,
    'å': unicSmallIe,
    'æ': unicSmallZhe,
    'ç': '\u0437',
    'è': unicSmallI,
    'é': '\u0439',
    'ê': '\u043A',
    'ë': unicSmallEl,
    'ì': '\u043C',
    'í': '\u043D',
    'î': unicSmallO,
    'ï': '\u043F',
    'ð': unicSmallEr,
    'ñ': unicSmallEs,
    'ò': unicSmallTe,
    'ó': unicSmallU,
    'ô': unicSmallEf,
    'õ': unicSmallHa,
    'ö': '\u0446',
    '÷': unicSmallChe,
    'ø': '\u0448',
    'ù': '\u0449',
    'ú': '\u044A',
    'û': unicSmallYeru,
    'ü': '\u044C',
    'ý': '\u044D',
    'þ': '\u044E',
    'ÿ': unicSmallLittleYus,
    'Œ': unicSmallUkrIWithDot,
    'Š': n_under + Pokrytie,
    'ƒ': '\u0027',
    'ˆ': '\u0485',
    'μ': '\u2DE8',
    'Ё': Titlo,
    'Ѓ': '\u2DF0' + Pokrytie,
    'Ќ': s_under + Pokrytie,
    'У': unicCapitalMonogrUk,
    'Я': unicCapitalLittleYus,
    'я': unicSmallLittleYus,
    'ё': erok_comb,
    '‐': '\u002D',
    '–': '\u0027',
    '‘': Oxia,
    '’': Oxia,
    '“': '\u030F',
    '”': '\u030F',
    '„': '\u2DE6' + Pokrytie,
    '†': CrossOrthodox,
    '‡': CrossOrthodox,
    '…': '\u2DE7' + Pokrytie,
    '‰': Kendema,
    '‹': zh_under,
    '™': x_under,
}
# ========================================

