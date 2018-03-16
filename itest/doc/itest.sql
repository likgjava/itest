/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50018
Source Host           : localhost:3306
Source Database       : itest

Target Server Type    : MYSQL
Target Server Version : 50018
File Encoding         : 65001

Date: 2018-03-16 16:04:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for ams_api
-- ----------------------------
DROP TABLE IF EXISTS `ams_api`;
CREATE TABLE `ams_api` (
  `id` int(11) unsigned NOT NULL auto_increment,
  `apiName` varchar(255) collate utf8_bin default NULL,
  `apiURI` varchar(255) collate utf8_bin default NULL,
  `apiProtocol` varchar(10) collate utf8_bin default NULL,
  `apiMethod` varchar(10) collate utf8_bin default NULL,
  `apiRequestParamType` varchar(20) collate utf8_bin default 'formData' COMMENT '请求参数类型[formData:表单数据; raw:源数据]',
  `apiRequestRaw` text collate utf8_bin,
  `apiSuccessMock` text collate utf8_bin COMMENT '成功返回示例',
  `apiFailureMock` text collate utf8_bin COMMENT '失败返回示例',
  `apiStatus` tinyint(1) unsigned default '0',
  `updateUser_id` int(11) default '0',
  `updateTime` timestamp NOT NULL default CURRENT_TIMESTAMP,
  `createTime` datetime default NULL COMMENT '创建时间',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of ams_api
-- ----------------------------
INSERT INTO `ams_api` VALUES ('19', '获取用户信息', 'www.baidu.com', 'HTTP', 'POST', 'formData', '', null, null, '0', '0', '2018-03-14 10:15:41', null);
INSERT INTO `ams_api` VALUES ('21', '添加用户2', 'www.baidu.com', 'HTTP', 'POST', 'formData', '', null, null, '0', '0', '2018-03-14 10:48:49', null);
INSERT INTO `ams_api` VALUES ('23', '添加用户4', 'www.baidu.com', 'HTTP', 'POST', 'formData', '', null, null, '0', '0', '2018-03-14 10:50:43', '2018-03-14 02:50:43');
INSERT INTO `ams_api` VALUES ('25', 'aaaaaa', 'www.baidu.com', 'HTTP', 'POST', 'formData', '', null, null, '0', '0', '2018-03-14 13:39:10', '2018-03-14 13:39:10');
INSERT INTO `ams_api` VALUES ('27', 'baidu2', 'www.baidu.com', 'HTTP', 'POST', 'formData', '', null, null, '0', '0', '2018-03-14 13:41:09', '2018-03-14 13:41:09');
INSERT INTO `ams_api` VALUES ('28', 'baidu111', 'www.163.com', 'HTTP', 'POST', 'formData', '', null, null, '0', '0', '2018-03-14 13:46:50', '2018-03-14 13:46:50');
INSERT INTO `ams_api` VALUES ('32', 'baidu111', 'www.163.com', 'HTTP', 'POST', 'formData', '', null, null, '0', '0', '2018-03-14 14:03:01', '2018-03-14 14:03:01');
INSERT INTO `ams_api` VALUES ('34', 'baidu111', 'www.163.com', 'HTTP', 'POST', 'formData', '', null, null, '0', '0', '2018-03-14 14:05:21', '2018-03-14 14:05:21');
INSERT INTO `ams_api` VALUES ('35', 'baidu111', 'www.163.com', 'HTTP', 'POST', 'formData', '', null, null, '0', '0', '2018-03-14 14:06:44', '2018-03-14 14:06:44');
INSERT INTO `ams_api` VALUES ('36', 'baidu111222', 'www.163.com', 'HTTP', 'POST', 'formData', '', null, null, '0', '0', '2018-03-14 14:13:11', '2018-03-14 14:13:11');
INSERT INTO `ams_api` VALUES ('38', '阳光易购', 'www.ebid360.com', 'HTTP', 'POST', 'raw', 0x61616161616161616161616262626262626262626262626262626262626262626262, 0x616161616161616161616161, 0x626262626262, '0', '0', '2018-03-14 16:43:36', '2018-03-14 16:43:36');
INSERT INTO `ams_api` VALUES ('39', 'fdsafdsafsadfdsaf', 'fdasfsadfsa', 'HTTP', 'POST', 'formData', '', '', '', '0', '0', '2018-03-15 09:45:58', '2018-03-15 09:45:58');
INSERT INTO `ams_api` VALUES ('40', 'aa', 'aa', 'HTTP', 'POST', 'formData', '', '', '', '0', '3', '2018-03-16 14:16:32', '2018-03-16 14:16:32');
INSERT INTO `ams_api` VALUES ('41', 'b', 'b', 'HTTP', 'POST', 'formData', '', '', '', '0', '3', '2018-03-16 15:07:30', '2018-03-16 15:07:30');
INSERT INTO `ams_api` VALUES ('42', '加法接口测试', '127.0.0.1:8000/test/add/', 'HTTP', 'POST', 'formData', '', 0x33, '', '0', '4', '2018-03-16 15:45:53', '2018-03-16 15:45:53');

-- ----------------------------
-- Table structure for ams_api_header
-- ----------------------------
DROP TABLE IF EXISTS `ams_api_header`;
CREATE TABLE `ams_api_header` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `headerName` varchar(255) default NULL,
  `headerValue` text,
  `apiID` int(10) unsigned default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ams_api_header
-- ----------------------------
INSERT INTO `ams_api_header` VALUES ('15', 'a', 'b', '19');
INSERT INTO `ams_api_header` VALUES ('17', 'a', 'b', '21');
INSERT INTO `ams_api_header` VALUES ('19', 'a', 'b', '23');
INSERT INTO `ams_api_header` VALUES ('21', 'a', 'b', '25');
INSERT INTO `ams_api_header` VALUES ('23', 'a', 'b', '27');
INSERT INTO `ams_api_header` VALUES ('24', 'a', 'b', '28');
INSERT INTO `ams_api_header` VALUES ('28', 'a', 'b', '32');
INSERT INTO `ams_api_header` VALUES ('30', 'a', 'b', '34');
INSERT INTO `ams_api_header` VALUES ('31', 'a', 'b', '35');
INSERT INTO `ams_api_header` VALUES ('32', 'a', 'b', '36');
INSERT INTO `ams_api_header` VALUES ('34', 'area', '010', '38');
INSERT INTO `ams_api_header` VALUES ('35', 'uid', '10001', '38');
INSERT INTO `ams_api_header` VALUES ('36', 'Accept', 'aaa', '39');
INSERT INTO `ams_api_header` VALUES ('37', 'a', 'a', '40');
INSERT INTO `ams_api_header` VALUES ('38', 'b', 'b', '41');

-- ----------------------------
-- Table structure for ams_api_request_param
-- ----------------------------
DROP TABLE IF EXISTS `ams_api_request_param`;
CREATE TABLE `ams_api_request_param` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `paramName` varchar(255) collate utf8_bin default NULL,
  `paramValue` varchar(255) collate utf8_bin default NULL,
  `paramType` tinyint(3) unsigned default '0',
  `apiID` int(10) unsigned default NULL,
  `paramNotNull` tinyint(1) default '0',
  PRIMARY KEY  (`id`),
  KEY `apiID` (`apiID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of ams_api_request_param
-- ----------------------------
INSERT INTO `ams_api_request_param` VALUES ('11', 'cc', 'dd', '0', '19', '0');
INSERT INTO `ams_api_request_param` VALUES ('13', 'cc', 'dd', '0', '21', '0');
INSERT INTO `ams_api_request_param` VALUES ('15', 'cc', 'dd', '0', '23', '0');
INSERT INTO `ams_api_request_param` VALUES ('17', 'cc', 'dd', '0', '25', '0');
INSERT INTO `ams_api_request_param` VALUES ('19', 'cc', 'dd', '0', '27', '0');
INSERT INTO `ams_api_request_param` VALUES ('20', 'cc', 'dd', '0', '28', '0');
INSERT INTO `ams_api_request_param` VALUES ('21', 'cc', 'dd', '0', '32', '0');
INSERT INTO `ams_api_request_param` VALUES ('23', 'cc', 'dd', '0', '34', '0');
INSERT INTO `ams_api_request_param` VALUES ('24', 'cc', 'dd', '0', '35', '0');
INSERT INTO `ams_api_request_param` VALUES ('25', 'cc', 'dd', '0', '36', '0');
INSERT INTO `ams_api_request_param` VALUES ('26', 'a', '111', '0', '39', '0');
INSERT INTO `ams_api_request_param` VALUES ('29', 'a', '1', '0', '42', '0');
INSERT INTO `ams_api_request_param` VALUES ('30', 'b', '2', '0', '42', '0');

-- ----------------------------
-- Table structure for ams_user
-- ----------------------------
DROP TABLE IF EXISTS `ams_user`;
CREATE TABLE `ams_user` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `userName` varchar(60) NOT NULL,
  `userPassword` varchar(60) NOT NULL,
  `userNickName` varchar(16) NOT NULL default '',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ams_user
-- ----------------------------
INSERT INTO `ams_user` VALUES ('1', 'abc', '1', '1');
INSERT INTO `ams_user` VALUES ('2', 'java', '1', '222');
INSERT INTO `ams_user` VALUES ('3', 'tom', '1', 'tom');
INSERT INTO `ams_user` VALUES ('4', 'rabbit', '1', '');
