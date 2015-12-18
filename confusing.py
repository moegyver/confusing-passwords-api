#!/usr/bin/env python 
# coding=utf-8

import random
import math
substitutions = {
    u"!": [
        {
            u"\uff01": u"U+FF01"
        }
    ],
    u"\"": [
        {
            u"\u2033": u"U+2033"
        },
        {
            u"\uff02": u"U+FF02"
        }
    ],
    u"$": [
        {
            u"\uff04": u"U+FF04"
        }
    ],
    u"%": [
        {
            u"\uff05": u"U+FF05"
        }
    ],
    u"&": [
        {
            u"\uff06": u"U+FF06"
        }
    ],
    u"'": [
        {
            u"\uff07": u"U+FF07"
        }
    ],
    u"(": [
        {
            u"\uff08": u"U+FF08"
        }
    ],
    u")": [
        {
            u"\uff09": u"U+FF09"
        }
    ],
    u"*": [
        {
            u"\u204e": u"U+204E"
        },
        {
            u"\uff0a": u"U+FF0A"
        }
    ],
    u"+": [
        {
            u"\uff0b": u"U+FF0B"
        }
    ],
    u",": [
        {
            u"\u201a": u"U+201A"
        },
        {
            u"\uff0c": u"U+FF0C"
        }
    ],
    u"-": [
        {
            u"\u2010": u"U+2010"
        },
        {
            u"\uff0d": u"U+FF0D"
        }
    ],
    u".": [
        {
            u"\uff0e": u"U+FF0E"
        }
    ],
    u"/": [
        {
            u"\u2044": u"U+2044"
        },
        {
            u"\uff0f": u"U+FF0F"
        }
    ],
    u"0": [
        {
            u"\uff10": u"U+FF10"
        }
    ],
    u"1": [
        {
            u"\uff11": u"U+FF11"
        }
    ],
    u"2": [
        {
            u"\uff12": u"U+FF12"
        }
    ],
    u"3": [
        {
            u"\uff13": u"U+FF13"
        }
    ],
    u"4": [
        {
            u"\uff14": u"U+FF14"
        }
    ],
    u"5": [
        {
            u"\uff15": u"U+FF15"
        }
    ],
    u"6": [
        {
            u"\uff16": u"U+FF16"
        }
    ],
    u"7": [
        {
            u"\uff17": u"U+FF17"
        }
    ],
    u"8": [
        {
            u"\uff18": u"U+FF18"
        }
    ],
    u"9": [
        {
            u"\uff19": u"U+FF19"
        }
    ],
    u":": [
        {
            u"\uff1a": u"U+FF1A"
        }
    ],
    u";": [
        {
            u"\u037e": u"U+037E"
        },
        {
            u"\uff1b": u"U+FF1B"
        }
    ],
    u"<": [
        {
            u"\u2039": u"U+2039"
        },
        {
            u"\uff1c": u"U+FF1C"
        }
    ],
    u"=": [
        {
            u"\uff1d": u"U+FF1D"
        }
    ],
    u">": [
        {
            u"\u203a": u"U+203A"
        },
        {
            u"\uff1e": u"U+FF1E"
        }
    ],
    u"?": [
        {
            u"\uff1f": u"U+FF1F"
        }
    ],
    u"@": [
        {
            u"\uff20": u"U+FF20"
        }
    ],
    u"A": [
        {
            u"\u0391": u"U+0391"
        },
        {
            u"\u0410": u"U+0410"
        },
        {
            u"\uff21": u"U+FF21"
        }
    ],
    u"B": [
        {
            u"\u0392": u"U+0392"
        },
        {
            u"\u0412": u"U+0412"
        },
        {
            u"\uff22": u"U+FF22"
        }
    ],
    u"C": [
        {
            u"\u03f9": u"U+03F9"
        },
        {
            u"\u0421": u"U+0421"
        },
        {
            u"\u216d": u"U+216D"
        },
        {
            u"\uff23": u"U+FF23"
        }
    ],
    u"D": [
        {
            u"\u216e": u"U+216E"
        },
        {
            u"\uff24": u"U+FF24"
        }
    ],
    u"E": [
        {
            u"\u0395": u"U+0395"
        },
        {
            u"\u0415": u"U+0415"
        },
        {
            u"\uff25": u"U+FF25"
        }
    ],
    u"F": [
        {
            u"\u03dc": u"U+03DC"
        },
        {
            u"\uff26": u"U+FF26"
        }
    ],
    u"G": [
        {
            u"\u050c": u"U+050C"
        },
        {
            u"\uff27": u"U+FF27"
        }
    ],
    u"H": [
        {
            u"\u0397": u"U+0397"
        },
        {
            u"\u041d": u"U+041D"
        },
        {
            u"\uff28": u"U+FF28"
        }
    ],
    u"I": [
        {
            u"\u0399": u"U+0399"
        },
        {
            u"\u0406": u"U+0406"
        },
        {
            u"\u2160": u"U+2160"
        },
        {
            u"\uff29": u"U+FF29"
        }
    ],
    u"J": [
        {
            u"\u0408": u"U+0408"
        },
        {
            u"\uff2a": u"U+FF2A"
        }
    ],
    u"K": [
        {
            u"\u039a": u"U+039A"
        },
        {
            u"\u041a": u"U+041A"
        },
        {
            u"\u212a": u"U+212A"
        },
        {
            u"\uff2b": u"U+FF2B"
        }
    ],
    u"L": [
        {
            u"\u216c": u"U+216C"
        },
        {
            u"\uff2c": u"U+FF2C"
        }
    ],
    u"M": [
        {
            u"\u039c": u"U+039C"
        },
        {
            u"\u041c": u"U+041C"
        },
        {
            u"\u216f": u"U+216F"
        },
        {
            u"\uff2d": u"U+FF2D"
        }
    ],
    u"N": [
        {
            u"\u039d": u"U+039D"
        },
        {
            u"\uff2e": u"U+FF2E"
        }
    ],
    u"O": [
        {
            u"\u039f": u"U+039F"
        },
        {
            u"\u041e": u"U+041E"
        },
        {
            u"\uff2f": u"U+FF2F"
        }
    ],
    u"P": [
        {
            u"\u03a1": u"U+03A1"
        },
        {
            u"\u0420": u"U+0420"
        },
        {
            u"\uff30": u"U+FF30"
        }
    ],
    u"Q": [
        {
            u"\uff31": u"U+FF31"
        }
    ],
    u"R": [
        {
            u"\uff32": u"U+FF32"
        }
    ],
    u"S": [
        {
            u"\u0405": u"U+0405"
        },
        {
            u"\uff33": u"U+FF33"
        }
    ],
    u"T": [
        {
            u"\u03a4": u"U+03A4"
        },
        {
            u"\u0422": u"U+0422"
        },
        {
            u"\uff34": u"U+FF34"
        }
    ],
    u"U": [
        {
            u"\uff35": u"U+FF35"
        }
    ],
    u"V": [
        {
            u"\u0474": u"U+0474"
        },
        {
            u"\u2164": u"U+2164"
        },
        {
            u"\uff36": u"U+FF36"
        }
    ],
    u"W": [
        {
            u"\uff37": u"U+FF37"
        }
    ],
    u"X": [
        {
            u"\u03a7": u"U+03A7"
        },
        {
            u"\u0425": u"U+0425"
        },
        {
            u"\u2169": u"U+2169"
        },
        {
            u"\uff38": u"U+FF38"
        }
    ],
    u"Y": [
        {
            u"\u03a5": u"U+03A5"
        },
        {
            u"\u04ae": u"U+04AE"
        },
        {
            u"\uff39": u"U+FF39"
        }
    ],
    u"Z": [
        {
            u"\u0396": u"U+0396"
        },
        {
            u"\uff3a": u"U+FF3A"
        }
    ],
    u"[": [
        {
            u"\uff3b": u"U+FF3B"
        }
    ],
    u"\\": [
        {
            u"\uff3c": u"U+FF3C"
        }
    ],
    u"]": [
        {
            u"\uff3d": u"U+FF3D"
        }
    ],
    u"^": [
        {
            u"\uff3e": u"U+FF3E"
        }
    ],
    u"_": [
        {
            u"\uff3f": u"U+FF3F"
        }
    ],
    u"`": [
        {
            u"\uff40": u"U+FF40"
        }
    ],
    u"a": [
        {
            u"\u0430": u"U+0430"
        },
        {
            u"\uff41": u"U+FF41"
        }
    ],
    u"b": [
        {
            u"\u042c": u"U+042C"
        },
        {
            u"\uff42": u"U+FF42"
        }
    ],
    u"c": [
        {
            u"\u03f2": u"U+03F2"
        },
        {
            u"\u0441": u"U+0441"
        },
        {
            u"\u217d": u"U+217D"
        },
        {
            u"\uff43": u"U+FF43"
        }
    ],
    u"d": [
        {
            u"\u0501": u"U+0501"
        },
        {
            u"\u217e": u"U+217E"
        },
        {
            u"\uff44": u"U+FF44"
        }
    ],
    u"e": [
        {
            u"\u0435": u"U+0435"
        },
        {
            u"\uff45": u"U+FF45"
        }
    ],
    u"f": [
        {
            u"\uff46": u"U+FF46"
        }
    ],
    u"g": [
        {
            u"\uff47": u"U+FF47"
        }
    ],
    u"h": [
        {
            u"\u04bb": u"U+04BB"
        },
        {
            u"\uff48": u"U+FF48"
        }
    ],
    u"i": [
        {
            u"\u0456": u"U+0456"
        },
        {
            u"\u2170": u"U+2170"
        },
        {
            u"\uff49": u"U+FF49"
        }
    ],
    u"j": [
        {
            u"\u0458": u"U+0458"
        },
        {
            u"\uff4a": u"U+FF4A"
        }
    ],
    u"k": [
        {
            u"\uff4b": u"U+FF4B"
        }
    ],
    u"l": [
        {
            u"\u217c": u"U+217C"
        },
        {
            u"\uff4c": u"U+FF4C"
        }
    ],
    u"m": [
        {
            u"\u217f": u"U+217F"
        },
        {
            u"\uff4d": u"U+FF4D"
        }
    ],
    u"n": [
        {
            u"\uff4e": u"U+FF4E"
        }
    ],
    u"o": [
        {
            u"\u03bf": u"U+03BF"
        },
        {
            u"\u043e": u"U+043E"
        },
        {
            u"\uff4f": u"U+FF4F"
        }
    ],
    u"p": [
        {
            u"\u0440": u"U+0440"
        },
        {
            u"\uff50": u"U+FF50"
        }
    ],
    u"q": [
        {
            u"\uff51": u"U+FF51"
        }
    ],
    u"r": [
        {
            u"\uff52": u"U+FF52"
        }
    ],
    u"s": [
        {
            u"\u0455": u"U+0455"
        },
        {
            u"\uff53": u"U+FF53"
        }
    ],
    u"t": [
        {
            u"\uff54": u"U+FF54"
        }
    ],
    u"u": [
        {
            u"\uff55": u"U+FF55"
        }
    ],
    u"v": [
        {
            u"\u03bd": u"U+03BD"
        },
        {
            u"\u0475": u"U+0475"
        },
        {
            u"\u2174": u"U+2174"
        },
        {
            u"\uff56": u"U+FF56"
        }
    ],
    u"w": [
        {
            u"\u0461": u"U+0461"
        },
        {
            u"\uff57": u"U+FF57"
        }
    ],
    u"x": [
        {
            u"\u0445": u"U+0445"
        },
        {
            u"\u2179": u"U+2179"
        },
        {
            u"\uff58": u"U+FF58"
        }
    ],
    u"y": [
        {
            u"\u0443": u"U+0443"
        },
        {
            u"\uff59": u"U+FF59"
        }
    ],
    u"z": [
        {
            u"\uff5a": u"U+FF5A"
        }
    ],
    u"{": [
        {
            u"\uff5b": u"U+FF5B"
        }
    ],
    u"|": [
        {
            u"\uff5c": u"U+FF5C"
        }
    ],
    u"}": [
        {
            u"\uff5d": u"U+FF5D"
        }
    ],
    u"~": [
        {
            u"\u2053": u"U+2053"
        },
        {
            u"\uff5e": u"U+FF5E"
        }
    ],
    u"\u00c4": [
        {
            u"\u04d2": u"U+04D2"
        }
    ],
    u"\u00d6": [
        {
            u"\u04e6": u"U+04E6"
        }
    ],
    u"\u00df": [
        {
            u"\u03b2": u"U+03B2"
        }
    ],
    u"\u00e4": [
        {
            u"\u04d3": u"U+04D3"
        }
    ],
    u"\u00f6": [
        {
            u"\u04e7": u"U+04E7"
        }
    ]
}


def replaceChar(character):
    if character in substitutions and random.random() > 0.5:
        key, value = substitutions[character][int(math.floor(random.random() * len(substitutions[character])))].items()[0]
        return key
    else:
        return character

def replace(input):
    result = u''
    for i in range(len(input)):
        result += replaceChar(input[i])
    return result

def lambda_handler(event, context):
    password = event['password']
    random.seed()
    return replace(password)
