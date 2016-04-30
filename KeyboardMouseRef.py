'''
Dictionaries and Arrays between
	PygameString,
	IntASCII,
	ASCII,
	CommonName,
	MouseInt,
	MouseString
'''


from pygame.locals import *

class KeyboardMouseRef:
	def __init__(self):
		self.IntASCII = [K_BACKSPACE,K_TAB,K_CLEAR,K_RETURN,K_PAUSE,K_ESCAPE,K_SPACE,K_EXCLAIM,K_QUOTEDBL,K_HASH,K_DOLLAR,K_AMPERSAND,K_QUOTE,K_LEFTPAREN,K_RIGHTPAREN,K_ASTERISK,K_PLUS,K_COMMA,K_MINUS,K_PERIOD,K_SLASH,K_0,K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_9,K_COLON,K_SEMICOLON,K_LESS,K_EQUALS,K_GREATER,K_QUESTION,K_AT,K_LEFTBRACKET,K_BACKSLASH,K_RIGHTBRACKET,K_CARET,K_UNDERSCORE,K_BACKQUOTE,K_a,K_b,K_c,K_d,K_e,K_f,K_g,K_h,K_i,K_j,K_k,K_l,K_m,K_n,K_o,K_p,K_q,K_r,K_s,K_t,K_u,K_v,K_w,K_x,K_y,K_z,K_DELETE,K_KP0,K_KP1,K_KP2,K_KP3,K_KP4,K_KP5,K_KP6,K_KP7,K_KP8,K_KP9,K_KP_PERIOD,K_KP_DIVIDE,K_KP_MULTIPLY,K_KP_MINUS,K_KP_PLUS,K_KP_ENTER,K_KP_EQUALS,K_UP,K_DOWN,K_RIGHT,K_LEFT,K_INSERT,K_HOME,K_END,K_PAGEUP,K_PAGEDOWN,K_F1,K_F2,K_F3,K_F4,K_F5,K_F6,K_F7,K_F8,K_F9,K_F10,K_F11,K_F12,K_F13,K_F14,K_F15,K_NUMLOCK,K_CAPSLOCK,K_SCROLLOCK,K_RSHIFT,K_LSHIFT,K_RCTRL,K_LCTRL,K_RALT,K_LALT,K_RMETA,K_LMETA,K_LSUPER,K_RSUPER,K_MODE,K_HELP,K_PRINT,K_SYSREQ,K_BREAK,K_MENU,K_POWER,K_EURO]
		self.PygameString = ["K_BACKSPACE ","K_TAB ","K_CLEAR ","K_RETURN ","K_PAUSE ","K_ESCAPE ","K_SPACE ","K_EXCLAIM ","K_QUOTEDBL ","K_HASH ","K_DOLLAR ","K_AMPERSAND ","K_QUOTE ","K_LEFTPAREN ","K_RIGHTPAREN ","K_ASTERISK ","K_PLUS ","K_COMMA ","K_MINUS ","K_PERIOD ","K_SLASH ","K_0 ","K_1 ","K_2 ","K_3 ","K_4 ","K_5 ","K_6 ","K_7 ","K_8 ","K_9 ","K_COLON ","K_SEMICOLON ","K_LESS ","K_EQUALS ","K_GREATER ","K_QUESTION ","K_AT ","K_LEFTBRACKET ","K_BACKSLASH ","K_RIGHTBRACKET ","K_CARET ","K_UNDERSCORE ","K_BACKQUOTE ","K_a ","K_b ","K_c ","K_d ","K_e ","K_f ","K_g ","K_h ","K_i ","K_j ","K_k ","K_l ","K_m ","K_n ","K_o ","K_p ","K_q ","K_r ","K_s ","K_t ","K_u ","K_v ","K_w ","K_x ","K_y ","K_z ","K_DELETE ","K_KP0 ","K_KP1 ","K_KP2 ","K_KP3 ","K_KP4 ","K_KP5 ","K_KP6 ","K_KP7 ","K_KP8 ","K_KP9 ","K_KP_PERIOD ","K_KP_DIVIDE ","K_KP_MULTIPLY ","K_KP_MINUS ","K_KP_PLUS ","K_KP_ENTER ","K_KP_EQUALS ","K_UP ","K_DOWN ","K_RIGHT ","K_LEFT ","K_INSERT ","K_HOME ","K_END ","K_PAGEUP ","K_PAGEDOWN ","K_F1 ","K_F2 ","K_F3 ","K_F4 ","K_F5 ","K_F6 ","K_F7 ","K_F8 ","K_F9 ","K_F10 ","K_F11 ","K_F12 ","K_F13 ","K_F14 ","K_F15 ","K_NUMLOCK ","K_CAPSLOCK ","K_SCROLLOCK ","K_RSHIFT ","K_LSHIFT ","K_RCTRL ","K_LCTRL ","K_RALT ","K_LALT ","K_RMETA ","K_LMETA ","K_LSUPER ","K_RSUPER ","K_MODE ","K_HELP ","K_PRINT ","K_SYSREQ ","K_BREAK ","K_MENU ","K_POWER ","K_EURO "]

#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	PygameString_CommonName
		self.PygameString_CommonName = {
			"K_BACKSPACE":"BACKSPACE",
			"K_TAB":"TAB",
			"K_CLEAR":"CLEAR",
			"K_RETURN":"RETURN",
			"K_PAUSE":"PAUSE",
			"K_ESCAPE":"ESCAPE",
			"K_SPACE":"SPACE",
			"K_EXCLAIM":"!",
			"K_QUOTEDBL":'"',
			"K_HASH":"#",
			"K_DOLLAR":"$",
			"K_AMPERSAND":"&",
			"K_QUOTE":"'",
			"K_LEFTPAREN":"(",
			"K_RIGHTPAREN":")",
			"K_ASTERISK":"*",
			"K_PLUS":"+",
			"K_COMMA":",",
			"K_MINUS":"-",
			"K_PERIOD":".",
			"K_SLASH":"/",
			"K_0":"0",
			"K_1":"1",
			"K_2":"2",
			"K_3":"3",
			"K_4":"4",
			"K_5":"5",
			"K_6":"6",
			"K_7":"7",
			"K_8":"8",
			"K_9":"9",
			"K_COLON":":",
			"K_SEMICOLON":";",
			"K_LESS":"<",
			"K_EQUALS":"=",
			"K_GREATER":">",
			"K_QUESTION":"?",
			"K_AT":"@",
			"K_LEFTBRACKET":"[",
			"K_BACKSLASH":"\\",
			"K_RIGHTBRACKET":"]",
			"K_CARET":"^",
			"K_UNDERSCORE":"_",
			"K_BACKQUOTE":"`",
			"K_a":"A",
			"K_b":"B",
			"K_c":"C",
			"K_d":"D",
			"K_e":"E",
			"K_f":"F",
			"K_g":"G",
			"K_h":"H",
			"K_i":"I",
			"K_j":"J",
			"K_k":"K",
			"K_l":"L",
			"K_m":"M",
			"K_n":"N",
			"K_o":"O",
			"K_p":"P",
			"K_q":"Q",
			"K_r":"R",
			"K_s":"S",
			"K_t":"T",
			"K_u":"U",
			"K_v":"V",
			"K_w":"W",
			"K_x":"X",
			"K_y":"Y",
			"K_z":"Z",
			"K_DELETE":"DELETE",
			"K_KP0":"KEYPAD 0",
			"K_KP1":"KEYPAD 1",
			"K_KP2":"KEYPAD 2",
			"K_KP3":"KEYPAD 3",
			"K_KP4":"KEYPAD 4",
			"K_KP5":"KEYPAD 5",
			"K_KP6":"KEYPAD 6",
			"K_KP7":"KEYPAD 7",
			"K_KP8":"KEYPAD 8",
			"K_KP9":"KEYPAD 9",
			"K_KP_PERIOD":"KEYPAD '.'",
			"K_KP_DIVIDE":"KEYPAD '/'",
			"K_KP_MULTIPLY":"KEYPAD '*'",
			"K_KP_MINUS":"KEYPAD '-'",
			"K_KP_PLUS":"KEYPAD '+'",
			"K_KP_ENTER":"KEYPAD ENTER",
			"K_KP_EQUALS":"KEYPAD '='",
			"K_UP":"UP",
			"K_DOWN":"DOWN",
			"K_RIGHT":"RIGHT",
			"K_LEFT":"LEFT",
			"K_INSERT":"INSERT",
			"K_HOME":"HOME",
			"K_END":"END",
			"K_PAGEUP":"PAGEUP",
			"K_PAGEDOWN":"PAGEDOWN",
			"K_F1":"F1",
			"K_F2":"F2",
			"K_F3":"F3",
			"K_F4":"F4",
			"K_F5":"F5",
			"K_F6":"F6",
			"K_F7":"F7",
			"K_F8":"F8",
			"K_F9":"F9",
			"K_F10":"F10",
			"K_F11":"F11",
			"K_F12":"F12",
			"K_F13":"F13",
			"K_F14":"F14",
			"K_F15":"F15",
			"K_NUMLOCK":"NUMLOCK",
			"K_CAPSLOCK":"CAPSLOCK",
			"K_SCROLLOCK":"SCROLLLOCK",
			"K_RSHIFT":"RIGHT SHIFT",
			"K_LSHIFT":"LEFT SHIFT",
			"K_RCTRL":"RIGHT CONTROL",
			"K_LCTRL":"LEFT CONTROL",
			"K_RALT":"RIGHT ALT",
			"K_LALT":"LEFT ALT",
			"K_RMETA":"RIGHT META",
			"K_LMETA":"LEFT META",
			"K_LSUPER":"LEFT SUPER",
			"K_RSUPER":"RIGHT SUPER",
			"K_MODE":"MODE",
			"K_HELP":"HELP",
			"K_PRINT":"PRINT",
			"K_SYSREQ":"SYSTEM REQUEST",
			"K_BREAK":"BREAK",
			"K_MENU":"MENU",
			"K_POWER":"POWER",
			"K_EURO":"EURO",
		}
##	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	PygameString_IntASCII
		self.PygameString_IntASCII = {
			"K_BACKSPACE":8,
			"K_TAB":9,
			"K_CLEAR":12,
			"K_RETURN":13,
			"K_PAUSE":19,
			"K_ESCAPE":27,
			"K_SPACE":32,
			"K_EXCLAIM":33,
			"K_QUOTEDBL":34,
			"K_HASH":35,
			"K_DOLLAR":36,
			"K_AMPERSAND":38,
			"K_QUOTE":39,
			"K_LEFTPAREN":40,
			"K_RIGHTPAREN":41,
			"K_ASTERISK":42,
			"K_PLUS":43,
			"K_COMMA":44,
			"K_MINUS":45,
			"K_PERIOD":46,
			"K_SLASH":47,
			"K_0":48,
			"K_1":49,
			"K_2":50,
			"K_3":51,
			"K_4":52,
			"K_5":53,
			"K_6":54,
			"K_7":55,
			"K_8":56,
			"K_9":57,
			"K_COLON":58,
			"K_SEMICOLON":59,
			"K_LESS":60,
			"K_EQUALS":61,
			"K_GREATER":62,
			"K_QUESTION":63,
			"K_AT":64,
			"K_LEFTBRACKET":91,
			"K_BACKSLASH":92,
			"K_RIGHTBRACKET":93,
			"K_CARET":94,
			"K_UNDERSCORE":95,
			"K_BACKQUOTE":96,
			"K_a":97,
			"K_b":98,
			"K_c":99,
			"K_d":100,
			"K_e":101,
			"K_f":102,
			"K_g":103,
			"K_h":104,
			"K_i":105,
			"K_j":106,
			"K_k":107,
			"K_l":108,
			"K_m":109,
			"K_n":110,
			"K_o":111,
			"K_p":112,
			"K_q":113,
			"K_r":114,
			"K_s":115,
			"K_t":116,
			"K_u":117,
			"K_v":118,
			"K_w":119,
			"K_x":120,
			"K_y":121,
			"K_z":122,
			"K_DELETE":127,
			"K_KP0":256,
			"K_KP1":257,
			"K_KP2":258,
			"K_KP3":259,
			"K_KP4":260,
			"K_KP5":261,
			"K_KP6":262,
			"K_KP7":263,
			"K_KP8":264,
			"K_KP9":265,
			"K_KP_PERIOD":266,
			"K_KP_DIVIDE":267,
			"K_KP_MULTIPLY":268,
			"K_KP_MINUS":269,
			"K_KP_PLUS":270,
			"K_KP_ENTER":271,
			"K_KP_EQUALS":272,
			"K_UP":273,
			"K_DOWN":274,
			"K_RIGHT":275,
			"K_LEFT":276,
			"K_INSERT":277,
			"K_HOME":278,
			"K_END":279,
			"K_PAGEUP":280,
			"K_PAGEDOWN":281,
			"K_F1":282,
			"K_F2":283,
			"K_F3":284,
			"K_F4":285,
			"K_F5":286,
			"K_F6":287,
			"K_F7":288,
			"K_F8":289,
			"K_F9":290,
			"K_F10":291,
			"K_F11":292,
			"K_F12":293,
			"K_F13":294,
			"K_F14":295,
			"K_F15":296,
			"K_NUMLOCK":300,
			"K_CAPSLOCK":301,
			"K_SCROLLOCK":302,
			"K_RSHIFT":303,
			"K_LSHIFT":304,
			"K_RCTRL":305,
			"K_LCTRL":306,
			"K_RALT":307,
			"K_LALT":308,
			"K_RMETA":309,
			"K_LMETA":310,
			"K_LSUPER":311,
			"K_RSUPER":312,
			"K_MODE":313,
			"K_HELP":315,
			"K_PRINT":316,
			"K_SYSREQ":317,
			"K_BREAK":318,
			"K_MENU":319,
			"K_POWER":320,
			"K_EURO":321
		}
##	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	IntASCII_PygameString
		self.IntASCII_PygameString = [
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			" K_BACKSPACE ",
			" K_TAB ",
			None,
			None,
			" K_CLEAR ",
			" K_RETURN ",
			None,
			None,
			None,
			None,
			None,
			" K_PAUSE ",
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			" K_ESCAPE ",
			None,
			None,
			None,
			None,
			" K_SPACE ",
			" K_EXCLAIM ",
			" K_QUOTEDBL ",
			" K_HASH ",
			" K_DOLLAR ",
			None,
			" K_AMPERSAND ",
			" K_QUOTE ",
			" K_LEFTPAREN ",
			" K_RIGHTPAREN ",
			" K_ASTERISK ",
			" K_PLUS ",
			" K_COMMA ",
			" K_MINUS ",
			" K_PERIOD ",
			" K_SLASH ",
			" K_0 ",
			" K_1 ",
			" K_2 ",
			" K_3 ",
			" K_4 ",
			" K_5 ",
			" K_6 ",
			" K_7 ",
			" K_8 ",
			" K_9 ",
			" K_COLON ",
			" K_SEMICOLON ",
			" K_LESS ",
			" K_EQUALS ",
			" K_GREATER ",
			" K_QUESTION ",
			" K_AT ",
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			" K_LEFTBRACKET ",
			" K_BACKSLASH ",
			" K_RIGHTBRACKET ",
			" K_CARET ",
			" K_UNDERSCORE ",
			" K_BACKQUOTE ",
			" K_a ",
			" K_b ",
			" K_c ",
			" K_d ",
			" K_e ",
			" K_f ",
			" K_g ",
			" K_h ",
			" K_i ",
			" K_j ",
			" K_k ",
			" K_l ",
			" K_m ",
			" K_n ",
			" K_o ",
			" K_p ",
			" K_q ",
			" K_r ",
			" K_s ",
			" K_t ",
			" K_u ",
			" K_v ",
			" K_w ",
			" K_x ",
			" K_y ",
			" K_z ",
			None,
			None,
			None,
			None,
			" K_DELETE ",
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			None,
			" K_KP0 ",
			" K_KP1 ",
			" K_KP2 ",
			" K_KP3 ",
			" K_KP4 ",
			" K_KP5 ",
			" K_KP6 ",
			" K_KP7 ",
			" K_KP8 ",
			" K_KP9 ",
			" K_KP_PERIOD ",
			" K_KP_DIVIDE ",
			" K_KP_MULTIPLY ",
			" K_KP_MINUS ",
			" K_KP_PLUS ",
			" K_KP_ENTER ",
			" K_KP_EQUALS ",
			" K_UP ",
			" K_DOWN ",
			" K_RIGHT ",
			" K_LEFT ",
			" K_INSERT ",
			" K_HOME ",
			" K_END ",
			" K_PAGEUP ",
			" K_PAGEDOWN ",
			" K_F1 ",
			" K_F2 ",
			" K_F3 ",
			" K_F4 ",
			" K_F5 ",
			" K_F6 ",
			" K_F7 ",
			" K_F8 ",
			" K_F9 ",
			" K_F10 ",
			" K_F11 ",
			" K_F12 ",
			" K_F13 ",
			" K_F14 ",
			" K_F15 ",
			None,
			None,
			None,
			" K_NUMLOCK ",
			" K_CAPSLOCK ",
			" K_SCROLLOCK ",
			" K_RSHIFT ",
			" K_LSHIFT ",
			" K_RCTRL ",
			" K_LCTRL ",
			" K_RALT ",
			" K_LALT ",
			" K_RMETA ",
			" K_LMETA ",
			" K_LSUPER ",
			" K_RSUPER ",
			" K_MODE ",
			None,
			" K_HELP ",
			" K_PRINT ",
			" K_SYSREQ ",
			" K_BREAK ",
			" K_MENU ",
			" K_POWER ",
			"K_EURO"
		]


		self.mouseInt_mouseString = [
		]
	
keyboardMouseRef = KeyboardMouseRef()