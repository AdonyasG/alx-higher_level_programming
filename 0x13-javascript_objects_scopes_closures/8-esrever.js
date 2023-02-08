#!/usr/bin/node
// 8-eserver.js

exports.esrever = function (list) {
	const listnew = [];

    for (i = list.length - 1; i >=0; i--) {
	    const index = list[i]
	    listnew.push(index)
    }
    return(listnew);
}
