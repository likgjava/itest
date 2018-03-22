/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50018
Source Host           : localhost:3306
Source Database       : itest

Target Server Type    : MYSQL
Target Server Version : 50018
File Encoding         : 65001

Date: 2018-03-22 23:08:25
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
  `group_id` int(11) default NULL COMMENT '接口分组id',
  `project_id` int(10) unsigned default NULL COMMENT '项目id',
  `updateUser_id` int(11) default '0',
  `updateTime` timestamp NOT NULL default CURRENT_TIMESTAMP,
  `createTime` datetime default NULL COMMENT '创建时间',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of ams_api
-- ----------------------------
INSERT INTO `ams_api` VALUES ('21', '两个数相加', 'localhost:8000/test/add?a=1&b=2', 'HTTP', 'GET', 'formData', '', 0x7B73756D3A337D, 0x4E6F6E65, '0', '1', '1', '4', '2018-03-22 14:46:35', '2018-03-22 14:46:35');
INSERT INTO `ams_api` VALUES ('38', '阳光易购', 'www.ebid360.com', 'HTTP', 'POST', 'raw', 0x61616161616161616161616262626262626262626262626262626262626262626262, 0x616161616161616161616161, 0x7BE28098636F6465E280993A313131317D, '0', null, '2', '5', '2018-03-21 15:19:41', '2018-03-21 15:19:41');
INSERT INTO `ams_api` VALUES ('40', 'aa', 'aa', 'HTTP', 'POST', 'formData', '', '', '', '0', null, '2', '3', '2018-03-16 14:16:32', '2018-03-16 14:16:32');
INSERT INTO `ams_api` VALUES ('42', '加法接口测试', '127.0.0.1:8000/test/add/', 'HTTP', 'POST', 'formData', '', 0x33, '', '0', null, '2', '4', '2018-03-16 15:45:53', '2018-03-16 15:45:53');

-- ----------------------------
-- Table structure for ams_api_group
-- ----------------------------
DROP TABLE IF EXISTS `ams_api_group`;
CREATE TABLE `ams_api_group` (
  `id` int(11) unsigned NOT NULL auto_increment,
  `groupName` varchar(30) collate utf8_bin NOT NULL,
  `project_id` int(11) unsigned NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `project_id` (`project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of ams_api_group
-- ----------------------------
INSERT INTO `ams_api_group` VALUES ('1', '加法', '1');
INSERT INTO `ams_api_group` VALUES ('3', '减法', '1');

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
INSERT INTO `ams_api_header` VALUES ('37', 'a', 'a', '40');
INSERT INTO `ams_api_header` VALUES ('39', 'area', '010', '38');
INSERT INTO `ams_api_header` VALUES ('40', 'uid', '10001', '38');
INSERT INTO `ams_api_header` VALUES ('45', 'area', '010', '21');

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
INSERT INTO `ams_api_request_param` VALUES ('29', 'a', '1', '0', '42', '0');
INSERT INTO `ams_api_request_param` VALUES ('30', 'b', '2', '0', '42', '0');
INSERT INTO `ams_api_request_param` VALUES ('34', 'a', '1', '0', '21', '0');
INSERT INTO `ams_api_request_param` VALUES ('35', 'b', '2', '0', '21', '0');

-- ----------------------------
-- Table structure for ams_api_result_param
-- ----------------------------
DROP TABLE IF EXISTS `ams_api_result_param`;
CREATE TABLE `ams_api_result_param` (
  `id` int(11) unsigned NOT NULL auto_increment,
  `paramName` varchar(255) collate utf8_bin default NULL,
  `paramValue` varchar(255) collate utf8_bin NOT NULL,
  `apiID` int(11) unsigned NOT NULL,
  `paramNotNull` tinyint(1) unsigned default NULL,
  PRIMARY KEY  (`id`),
  KEY `apiID` (`apiID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='接口返回参数';

-- ----------------------------
-- Records of ams_api_result_param
-- ----------------------------

-- ----------------------------
-- Table structure for ams_api_result_value
-- ----------------------------
DROP TABLE IF EXISTS `ams_api_result_value`;
CREATE TABLE `ams_api_result_value` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `value` text collate utf8_bin,
  `valueDesc` varchar(255) collate utf8_bin default NULL,
  `param_id` int(10) unsigned NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `resultParamID` (`param_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='接口返回参数内容';

-- ----------------------------
-- Records of ams_api_result_value
-- ----------------------------

-- ----------------------------
-- Table structure for ams_project
-- ----------------------------
DROP TABLE IF EXISTS `ams_project`;
CREATE TABLE `ams_project` (
  `id` int(11) unsigned NOT NULL auto_increment,
  `projectType` tinyint(1) unsigned default '0',
  `projectName` varchar(255) collate utf8_bin NOT NULL,
  `projectUpdateTime` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `projectVersion` varchar(6) collate utf8_bin NOT NULL default '1.0',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of ams_project
-- ----------------------------
INSERT INTO `ams_project` VALUES ('1', '0', '测试系统', '2018-03-22 14:22:54', '1.0');
INSERT INTO `ams_project` VALUES ('2', '0', '学生管理系统', '2018-03-21 15:21:50', '5.0');

-- ----------------------------
-- Table structure for ams_test_case
-- ----------------------------
DROP TABLE IF EXISTS `ams_test_case`;
CREATE TABLE `ams_test_case` (
  `id` int(11) NOT NULL auto_increment COMMENT '用例ID',
  `project_id` int(11) NOT NULL COMMENT '项目ID',
  `caseName` varchar(255) NOT NULL COMMENT '用例名称',
  `caseDesc` varchar(255) default NULL COMMENT '用例描述',
  `createUser_id` int(11) default NULL COMMENT '用户ID',
  `createTime` datetime default NULL COMMENT '创建时间',
  `updateTime` timestamp NOT NULL default CURRENT_TIMESTAMP COMMENT '更新时间',
  `group_id` int(11) default NULL COMMENT '分组ID',
  `caseType` tinyint(4) default '0' COMMENT '0表示简单，1表示高级',
  `caseCode` longtext,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ams_test_case
-- ----------------------------
INSERT INTO `ams_test_case` VALUES ('8', '1', '单接口测试-加法', null, null, null, '2018-03-22 16:13:37', '3', '0', null);

-- ----------------------------
-- Table structure for ams_test_case_group
-- ----------------------------
DROP TABLE IF EXISTS `ams_test_case_group`;
CREATE TABLE `ams_test_case_group` (
  `id` int(11) NOT NULL auto_increment COMMENT '分组ID',
  `groupName` varchar(100) NOT NULL COMMENT '组名',
  `project_id` int(11) NOT NULL COMMENT '项目ID',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ams_test_case_group
-- ----------------------------
INSERT INTO `ams_test_case_group` VALUES ('1', '范德萨', '2');
INSERT INTO `ams_test_case_group` VALUES ('2', '登录模块', '2');
INSERT INTO `ams_test_case_group` VALUES ('3', '加法测试用例', '1');

-- ----------------------------
-- Table structure for ams_test_case_item
-- ----------------------------
DROP TABLE IF EXISTS `ams_test_case_item`;
CREATE TABLE `ams_test_case_item` (
  `id` int(11) NOT NULL auto_increment COMMENT '关联ID',
  `case_id` int(11) NOT NULL COMMENT '用例ID',
  `caseData` text COMMENT '内容',
  `caseCode` text COMMENT '用例代码',
  `statusCode` varchar(20) default NULL,
  `matchType` tinyint(4) default '0' COMMENT '校验类型[0:不校验; 1:完全校验; 2:正则校验; 3:json校验]',
  `matchRule` text,
  `apiName` varchar(255) NOT NULL COMMENT '接口名称',
  `apiUri` varchar(255) NOT NULL COMMENT '接口路径',
  `apiMethod` varchar(10) default 'POST' COMMENT '请求方式',
  `apiProtocol` varchar(10) default NULL COMMENT '请求协议',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ams_test_case_item
-- ----------------------------
INSERT INTO `ams_test_case_item` VALUES ('8', '8', '{\"headers\": [{\"headerName\": \"area\", \"headerValue\": \"010\"}], \"apiUri\": \"localhost:8000/test/add?a=1&b=2\", \"apiProtocol\": \"HTTP\", \"apiMethod\": \"GET\", \"requestType\": \"formData\", \"params\": [{\"paramName\": \"a\", \"paramValue\": \"1\"}, {\"paramName\": \"b\", \"paramValue\": \"2\"}]}', null, '200', '1', '3', '两个数相加', 'localhost:8000/test/add?a=1&b=2', 'GET', 'HTTP');

-- ----------------------------
-- Table structure for ams_test_case_item_result
-- ----------------------------
DROP TABLE IF EXISTS `ams_test_case_item_result`;
CREATE TABLE `ams_test_case_item_result` (
  `id` int(11) NOT NULL auto_increment COMMENT 'id',
  `item_id` int(11) NOT NULL COMMENT '用例条目ID',
  `resultData` text COMMENT '测试结果内容',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ams_test_case_item_result
-- ----------------------------
INSERT INTO `ams_test_case_item_result` VALUES ('1', '8', '{\"url\": \"HTTP://localhost:8000/test/add?a=1&b=2\", \"apiMethod\": \"GET\", \"statusCode\": 200, \"headers\": {\"User-Agent\": \"python-requests/2.18.4\", \"Accept-Encoding\": \"gzip, deflate\", \"Accept\": \"*/*\", \"Connection\": \"keep-alive\", \"area\": \"010\"}, \"params\": {\"a\": \"1\", \"b\": \"2\"}, \"matchType\": 1, \"matchRule\": \"3\", \"returnBody\": \"{\\\"sum\\\": 3}\"}');
INSERT INTO `ams_test_case_item_result` VALUES ('2', '8', '{\"url\": \"HTTP://localhost:8000/test/add?a=1&b=2\", \"apiMethod\": \"GET\", \"statusCode\": 200, \"headers\": {\"User-Agent\": \"python-requests/2.18.4\", \"Accept-Encoding\": \"gzip, deflate\", \"Accept\": \"*/*\", \"Connection\": \"keep-alive\", \"area\": \"010\"}, \"params\": {\"a\": \"1\", \"b\": \"2\"}, \"matchType\": 1, \"matchRule\": \"3\", \"returnBody\": \"{\\\"sum\\\": 3}\"}');
INSERT INTO `ams_test_case_item_result` VALUES ('3', '8', '{\"url\": \"HTTP://localhost:8000/test/add?a=1&b=2\", \"apiMethod\": \"GET\", \"statusCode\": 200, \"headers\": {\"User-Agent\": \"python-requests/2.18.4\", \"Accept-Encoding\": \"gzip, deflate\", \"Accept\": \"*/*\", \"Connection\": \"keep-alive\", \"area\": \"010\"}, \"params\": {\"a\": \"1\", \"b\": \"2\"}, \"matchType\": 1, \"matchRule\": \"3\", \"returnBody\": \"{\\\"sum\\\": 3}\"}');
INSERT INTO `ams_test_case_item_result` VALUES ('4', '8', '{\"url\": \"HTTP://localhost:8000/test/add?a=1&b=2\", \"apiMethod\": \"GET\", \"statusCode\": 200, \"headers\": {\"User-Agent\": \"python-requests/2.18.4\", \"Accept-Encoding\": \"gzip, deflate\", \"Accept\": \"*/*\", \"Connection\": \"keep-alive\", \"area\": \"010\"}, \"params\": {\"a\": \"1\", \"b\": \"2\"}, \"matchType\": 1, \"matchRule\": \"3\", \"returnBody\": \"{\\\"sum\\\": 3}\"}');

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
INSERT INTO `ams_user` VALUES ('5', 'cici', '1', 'cici');
