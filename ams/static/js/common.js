var cookieUtil = {
    // 设置cookie
    setCookie: function (key, value, expireDays) {
        var cookie = key + '=' + encodeURI(value);
        if(expireDays != null){
            var date = new Date();
            date.setTime(date.getTime() + expireDays * 24 * 60 * 60 * 1000);
            cookie += ';expires=' + date.toGMTString();
        }
        document.cookie = cookie;
    },

    // 读取cookie
    getCookie: function (key) {
        console.log(document.cookie);
        if (document.cookie.length > 0) {
            var c_start = document.cookie.indexOf(key + "=");
            if (c_start !== -1) {
                c_start = c_start + key.length + 1;
                var c_end = document.cookie.indexOf(";", c_start);
                if (c_end === -1) {
                    c_end = document.cookie.length
                }
                return unescape(document.cookie.substring(c_start, c_end))
            }
        }
        return ""
    },

    // 删除cookie
    delCookie: function (key) {
        var exp = new Date();
        exp.setTime(exp.getTime() - 1);
        document.cookie = key + "=v;expires=" + exp.toGMTString();
    }
};