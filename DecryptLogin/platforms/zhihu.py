'''
Function:
	知乎模拟登录
		--https://www.zhihu.com/(PC端)
		--移动端暂不支持
Author:
	Charles
微信公众号:
	Charles的皮卡丘
GitHub:
	https://github.com/CharlesPikachu
更新日期:
	2020-01-28
'''
import os
import time
import hmac
import base64
import execjs
import hashlib
import requests
from ..utils.utils import *
from urllib.parse import urlencode


'''js code'''
encrypt_js_code = '''
// I borrowed the codes from https://github.com/zkqiang/zhihu-login/blob/master/encrypt.js
function s(e) {
	return (s = "function" == typeof Symbol && "symbol" == typeof Symbol.t ? function(e) {
			return typeof e
	}
	: function(e) {
			return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
	}
	)(e)
}
function i() {}
function h(e) {
	this.s = (2048 & e) >> 11,
	this.i = (1536 & e) >> 9,
	this.h = 511 & e,
	this.A = 511 & e
}
function A(e) {
	this.i = (3072 & e) >> 10,
	this.A = 1023 & e
}
function n(e) {
	this.n = (3072 & e) >> 10,
	this.e = (768 & e) >> 8,
	this.a = (192 & e) >> 6,
	this.s = 63 & e
}
function e(e) {
	this.i = e >> 10 & 3,
	this.h = 1023 & e
}
function a() {}
function c(e) {
	this.n = (3072 & e) >> 10,
	this.e = (768 & e) >> 8,
	this.a = (192 & e) >> 6,
	this.s = 63 & e
}
function o(e) {
	this.A = (4095 & e) >> 2,
	this.s = 3 & e
}
function r(e) {
	this.i = e >> 10 & 3,
	this.h = e >> 2 & 255,
	this.s = 3 & e
}
function k(e) {
	this.s = (4095 & e) >> 10,
	this.i = (1023 & e) >> 8,
	this.h = 1023 & e,
	this.A = 63 & e
}
function B(e) {
	this.s = (4095 & e) >> 10,
	this.n = (1023 & e) >> 8,
	this.e = (255 & e) >> 6
}
function f(e) {
	this.i = (3072 & e) >> 10,
	this.A = 1023 & e
}
function u(e) {
	this.A = 4095 & e
}
function C(e) {
	this.i = (3072 & e) >> 10
}
function b(e) {
	this.A = 4095 & e
}
function g(e) {
	this.s = (3840 & e) >> 8,
	this.i = (192 & e) >> 6,
	this.h = 63 & e
}
function G() {
	this.c = [0, 0, 0, 0],
	this.o = 0,
	this.r = [],
	this.k = [],
	this.B = [],
	this.f = [],
	this.u = [],
	this.C = !1,
	this.b = [],
	this.g = [],
	this.G = !1,
	this.Q = null,
	this.R = null,
	this.w = [],
	this.x = 0,
	this.D = {
			0: i,
			1: h,
			2: A,
			3: n,
			4: e,
			5: a,
			6: c,
			7: o,
			8: r,
			9: k,
			10: B,
			11: f,
			12: u,
			13: C,
			14: b,
			15: g
	}
}
Object.defineProperty(exports, "__esModule", {
	value: !0
});
var t = "1.1"
, __g = {};
i.prototype.M = function(e) {
	e.G = !1
}
,
h.prototype.M = function(e) {
	switch (this.s) {
	case 0:
			e.c[this.i] = this.h;
			break;
	case 1:
			e.c[this.i] = e.k[this.A]
	}
}
,
A.prototype.M = function(e) {
	e.k[this.A] = e.c[this.i]
}
,
n.prototype.M = function(e) {
	switch (this.s) {
	case 0:
			e.c[this.n] = e.c[this.e] + e.c[this.a];
			break;
	case 1:
			e.c[this.n] = e.c[this.e] - e.c[this.a];
			break;
	case 2:
			e.c[this.n] = e.c[this.e] * e.c[this.a];
			break;
	case 3:
			e.c[this.n] = e.c[this.e] / e.c[this.a];
			break;
	case 4:
			e.c[this.n] = e.c[this.e] % e.c[this.a];
			break;
	case 5:
			e.c[this.n] = e.c[this.e] == e.c[this.a];
			break;
	case 6:
			e.c[this.n] = e.c[this.e] >= e.c[this.a];
			break;
	case 7:
			e.c[this.n] = e.c[this.e] || e.c[this.a];
			break;
	case 8:
			e.c[this.n] = e.c[this.e] && e.c[this.a];
			break;
	case 9:
			e.c[this.n] = e.c[this.e] !== e.c[this.a];
			break;
	case 10:
			e.c[this.n] = s(e.c[this.e]);
			break;
	case 11:
			e.c[this.n] = e.c[this.e]in e.c[this.a];
			break;
	case 12:
			e.c[this.n] = e.c[this.e] > e.c[this.a];
			break;
	case 13:
			e.c[this.n] = -e.c[this.e];
			break;
	case 14:
			e.c[this.n] = e.c[this.e] < e.c[this.a];
			break;
	case 15:
			e.c[this.n] = e.c[this.e] & e.c[this.a];
			break;
	case 16:
			e.c[this.n] = e.c[this.e] ^ e.c[this.a];
			break;
	case 17:
			e.c[this.n] = e.c[this.e] << e.c[this.a];
			break;
	case 18:
			e.c[this.n] = e.c[this.e] >>> e.c[this.a];
			break;
	case 19:
			e.c[this.n] = e.c[this.e] | e.c[this.a]
	}
}
,
e.prototype.M = function(e) {
	e.r.push(e.o),
	e.B.push(e.k),
	e.o = e.c[this.i],
	e.k = [];
	for (var t = 0; t < this.h; t++)
			e.k.unshift(e.f.pop());
	e.u.push(e.f),
	e.f = []
}
,
a.prototype.M = function(e) {
	e.o = e.r.pop(),
	e.k = e.B.pop(),
	e.f = e.u.pop()
}
,
c.prototype.M = function(e) {
	switch (this.s) {
	case 0:
			e.C = e.c[this.n] >= e.c[this.e];
			break;
	case 1:
			e.C = e.c[this.n] <= e.c[this.e];
			break;
	case 2:
			e.C = e.c[this.n] > e.c[this.e];
			break;
	case 3:
			e.C = e.c[this.n] < e.c[this.e];
			break;
	case 4:
			e.C = e.c[this.n] == e.c[this.e];
			break;
	case 5:
			e.C = e.c[this.n] != e.c[this.e];
			break;
	case 6:
			e.C = e.c[this.n];
			break;
	case 7:
			e.C = !e.c[this.n]
	}
}
,
o.prototype.M = function(e) {
	switch (this.s) {
	case 0:
			e.o = this.A;
			break;
	case 1:
			e.C && (e.o = this.A);
			break;
	case 2:
			e.C || (e.o = this.A);
			break;
	case 3:
			e.o = this.A,
			e.Q = null
	}
	e.C = !1
}
,
r.prototype.M = function(e) {
	switch (this.s) {
	case 0:
			for (var t = [], n = 0; n < this.h; n++)
					t.unshift(e.f.pop());
			e.c[3] = e.c[this.i](t[0], t[1]);
			break;
	case 1:
			for (var r = e.f.pop(), o = [], i = 0; i < this.h; i++)
					o.unshift(e.f.pop());
			e.c[3] = e.c[this.i][r](o[0], o[1]);
			break;
	case 2:
			for (var a = [], c = 0; c < this.h; c++)
					a.unshift(e.f.pop());
			e.c[3] = new e.c[this.i](a[0],a[1])
	}
}
,
k.prototype.M = function(e) {
	switch (this.s) {
	case 0:
			e.f.push(e.c[this.i]);
			break;
	case 1:
			e.f.push(this.h);
			break;
	case 2:
			e.f.push(e.k[this.A]);
			break;
	case 3:
			e.f.push(e.g[this.A])
	}
}
,
B.prototype.M = function(t) {
	switch (this.s) {
	case 0:
			var s = t.f.pop();
			t.c[this.n] = t.c[this.e][s];
			break;
	case 1:
			var i = t.f.pop()
				, h = t.f.pop();
			t.c[this.e][i] = h;
			break;
	case 2:
			var A = t.f.pop();
			if(A === 'window') {
					A = {
							encodeURIComponent: function (url) {
									return encodeURIComponent(url)
							}
					}
			} else if (A === 'navigator') {
					A = {
							'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
									'(KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
					}
			}
			t.c[this.n] = eval(A)
	}
}
,
f.prototype.M = function(e) {
	e.c[this.i] = e.g[this.A]
}
,
u.prototype.M = function(e) {
	e.Q = this.A
}
,
C.prototype.M = function(e) {
	throw e.c[this.i]
}
,
b.prototype.M = function(e) {
	var t = this
		, n = [0];
	e.k.forEach(function(e) {
			n.push(e)
	});
	var r = function(r) {
			var o = new G;
			return o.k = n,
			o.k[0] = r,
			o.J(e.b, t.A, e.g, e.w),
			o.c[3]
	};
	r.toString = function() {
			return "() { [native code] }"
	}
	,
	e.c[3] = r
}
,
g.prototype.M = function(e) {
	switch (this.s) {
	case 0:
			for (var t = {}, n = 0; n < this.h; n++) {
					var r = e.f.pop();
					t[e.f.pop()] = r
			}
			e.c[this.i] = t;
			break;
	case 1:
			for (var o = [], i = 0; i < this.h; i++)
					o.unshift(e.f.pop());
			e.c[this.i] = o
	}
}
,
G.prototype.v = function(e) {
	for (var t = Buffer.from(e, 'base64').toString('binary'), n = [], r = 0; r < t.length - 1; r += 2)
			n.push(t.charCodeAt(r) << 8 | t.charCodeAt(r + 1));
	this.b = n
}
,
G.prototype.y = function(e) {
	for (var t = Buffer.from(e, 'base64').toString('binary'), n = 66, r = [], o = 0; o < t.length; o++) {
			var i = 24 ^ t.charCodeAt(o) ^ n;
			r.push(String.fromCharCode(i)),
			n = i
	}
	return r.join("")
}
,
G.prototype.F = function(e) {
	var t = this;
	this.g = e.map(function(e) {
			return "string" == typeof e ? t.y(e) : e
	})
}
,
G.prototype.J = function(e, t, n) {
	for (t = t || 0,
	n = n || [],
	this.o = t,
	"string" == typeof e ? (this.F(n),
	this.v(e)) : (this.b = e,
	this.g = n),
	this.G = !0,
	this.x = Date.now(); this.G; ) {
			var r = this.b[this.o++];
			if ("number" != typeof r)
					break;
			var o = Date.now();
			if (500 < o - this.x)
					return;
			this.x = o;
			try {
					this.M(r)
			} catch (e) {
					if (this.R = e,
					!this.Q)
							throw "execption at " + this.o + ": " + e;
					this.o = this.Q
			}
	}
}
,
G.prototype.M = function(e) {
	var t = (61440 & e) >> 12;
	new this.D[t](e).M(this)
}
,
(new G).J("4AeTAJwAqACcAaQAAAAYAJAAnAKoAJwDgAWTACwAnAKoACACGAESOTRHkQAkAbAEIAMYAJwFoAASAzREJAQYBBIBNEVkBnCiGAC0BjRAJAAYBBICNEVkBnDGGAC0BzRAJACwCJAAnAmoAJwKoACcC4ABnAyMBRAAMwZgBnESsA0aADRAkQAkABgCnA6gABoCnA+hQDRHGAKcEKAAMQdgBnFasBEaADRAkQAkABgCnBKgABoCnBOhQDRHZAZxkrAUGgA0QJEAJAAYApwVoABgBnG6sBYaADRAkQAkABgCnBegAGAGceKwGBoANECRACQAnAmoAJwZoABgBnIOsBoaADRAkQAkABgCnBugABoCnByhQDRHZAZyRrAdGgA0QJEAJAAQACAFsB4gBhgAnAWgABIBNEEkBxgHEgA0RmQGdJoQCBoFFAE5gCgFFAQ5hDSCJAgYB5AAGACcH4AFGAEaCDRSEP8xDzMQIAkQCBoFFAE5gCgFFAQ5hDSCkQAkCBgBGgg0UhD/MQ+QACAIGAkaBxQBOYGSABoAnB+EBRoIN1AUCDmRNJMkCRAIGgUUATmAKAUUBDmENIKRACQIGAEaCDRSEP8xD5AAIAgYCRoHFAI5gZIAGgCcH4QFGgg3UBQQOZE0kyQJGAMaCRQ/OY+SABoGnCCEBTTAJAMYAxoJFAY5khI/Nk+RABoGnCCEBTTAJAMYAxoJFAw5khI/Nk+RABoGnCCEBTTAJAMYAxoJFBI5khI/Nk+RABoGnCCEBTTAJAMYBxIDNEEkB3JsHgNQAA==", 0, ["BRgg", "BSITFQkTERw=", "LQYfEhMA", "PxMVFBMZKB8DEjQaBQcZExMC", "", "NhETEQsE", "Whg=", "Wg==", "MhUcHRARDhg=", "NBcPBxYeDQMF", "Lx4ODys+GhMC", "LgM7OwAKDyk6Cg4=", "Mx8SGQUvMQ==", "SA==", "ORoVGCQgERcCAxo=", "BTcAERcCAxo=", "BRg3ABEXAgMaFAo=", "SQ==", "OA8LGBsP", "GC8LGBsP", "Tg==", "PxAcBQ==", "Tw==", "KRsJDgE=", "TA==", "LQofHg4DBwsP", "TQ==", "PhMaNCwZAxoUDQUeGQ==", "PhMaNCwZAxoUDQUeGTU0GQIeBRsYEQ8=", "Qg==", "BWpUGxkfGRsZFxkbGR8ZGxkHGRsZHxkbGRcZG1MbGR8ZGxkXGRFpGxkfGRsZFxkbGR8ZGxkHGRsZHxkbGRcZGw==", "ORMRCyk0Exk8LQ==", "ORMRCyst"]);
var Q = function(e) {
	return __g._encrypt(e)
};
'''


'''
Function:
	知乎模拟登录
Detail:
	-login:
		Input:
			--username: 用户名
			--password: 密码
			--mode: mobile/pc
			--crackvc_func: 若提供验证码接口, 则利用该接口来实现验证码的自动识别
		Return:
			--infos_return: 用户名等信息
			--session: 登录后的requests.Session()
'''
class zhihu():
	def __init__(self, **kwargs):
		self.info = 'zhihu'
		self.cur_path = os.getcwd()
		self.session = requests.Session()
	'''登录函数'''
	def login(self, username, password, mode='pc', crackvc_func=None, **kwargs):
		if mode == 'mobile':
			return None
		elif mode == 'pc':
			self.__initializePC()
			# 验证码验证
			self.session.headers.update(self.headers)
			res = self.session.get(self.captcha_url)
			captcha = ''
			if 'true' in res.text:
				res = self.session.put(self.captcha_url)
				img_base64 = res.json()['img_base64'].replace('\\n', '')
				saveImage(base64.b64decode(img_base64), os.path.join(self.cur_path, 'captcha.jpg'))
				if crackvc_func is None:
					showImage(os.path.join(self.cur_path, 'captcha.jpg'))
					captcha = input('Input the Verification Code:')
				else:
					captcha = crackvc_func(os.path.join(self.cur_path, 'captcha.jpg'))
				self.session.post(self.captcha_url, data={'input_text': captcha})
			removeImage(os.path.join(self.cur_path, 'captcha.jpg'))
			# 获取_xsrf
			_xsrf = ''
			self.session.get(self.homepage_url, allow_redirects=False)
			for c in self.session.cookies:
				if c.name == '_xsrf':
					_xsrf = c.value
			# 获取signature
			signature = hmac.new(b'd1b964811afb40118a12068ff74a12f4', digestmod=hashlib.sha1)
			grant_type = 'password'
			client_id = 'c3cef7c66a1843f8b3a9e6a1e3160e20'
			source = 'com.zhihu.web'
			timestamp = str(int(time.time() * 1000))
			signature.update(bytes((grant_type+client_id+source+timestamp), 'utf-8'))
			signature = signature.hexdigest()
			data = {
					'client_id': client_id,
					'grant_type': grant_type,
					'source': source,
					'username': username,
					'password': password,
					'lang': 'en',
					'ref_source': 'homepage',
					'utm_source': '',
					'captcha': captcha,
					'timestamp': timestamp,
					'signature': signature
					}
			js = execjs.compile(encrypt_js_code)
			data = js.call('Q', urlencode(data))
			self.headers.update({'x-zse-83': '3_1.1', 'x-xsrftoken': _xsrf, 'content-type': 'application/x-www-form-urlencoded'})
			self.session.headers.update(self.headers)
			res = self.session.post(self.login_url, data=data)
			if 'user_id' in res.json():
				print('[INFO]: Account -> %s, login successfully...' % username)
				infos_return = {'username': username}
				return infos_return, self.session
			else:
				raise RuntimeError('Account -> %s, fail to login, username or password error...' % username)
		else:
			raise ValueError('Unsupport argument in zhihu.login -> mode %s, expect <mobile> or <pc>...' % mode)
	'''初始化PC端'''
	def __initializePC(self):
		self.headers = {
							'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
							'Referer': 'https://www.zhihu.com/',
							'Host': 'www.zhihu.com',
							'accept-encoding': 'gzip, deflate, br'
						}
		self.captcha_url = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=en'
		self.homepage_url = 'https://www.zhihu.com/'
		self.login_url = 'https://www.zhihu.com/api/v3/oauth/sign_in'
	'''初始化移动端'''
	def __initializeMobile(self):
		pass


'''test'''
if __name__ == '__main__':
	zhihu().login('', '')