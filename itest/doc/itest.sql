/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50018
Source Host           : localhost:3306
Source Database       : itest

Target Server Type    : MYSQL
Target Server Version : 50018
File Encoding         : 65001

Date: 2018-03-21 23:08:12
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
INSERT INTO `ams_api` VALUES ('19', '获取用户信息', 'www.baidu.com', 'HTTP', 'POST', 'formData', '', null, null, '0', null, '1', '0', '2018-03-14 10:15:41', null);
INSERT INTO `ams_api` VALUES ('21', '添加用户2', 'www.baidu.com', 'HTTP', 'POST', 'formData', '', null, null, '0', null, '1', '0', '2018-03-14 10:48:49', null);
INSERT INTO `ams_api` VALUES ('23', '添加用户4', 'www.baidu.com', 'HTTP', 'POST', 'formData', '', 0x4E6F6E65, 0x4E6F6E65, '0', '1', '1', '5', '2018-03-21 22:34:31', '2018-03-21 22:34:31');
INSERT INTO `ams_api` VALUES ('25', 'aaaaaa', 'www.baidu.com', 'HTTP', 'POST', 'formData', '', null, null, '0', null, '1', '0', '2018-03-14 13:39:10', '2018-03-14 13:39:10');
INSERT INTO `ams_api` VALUES ('27', 'baidu2', 'www.baidu.com', 'HTTP', 'POST', 'formData', '', null, null, '0', null, '1', '0', '2018-03-14 13:41:09', '2018-03-14 13:41:09');
INSERT INTO `ams_api` VALUES ('28', 'baidu111', 'www.163.com', 'HTTP', 'POST', 'formData', '', null, null, '0', null, '1', '0', '2018-03-14 13:46:50', '2018-03-14 13:46:50');
INSERT INTO `ams_api` VALUES ('32', 'baidu111', 'www.163.com', 'HTTP', 'POST', 'formData', '', null, null, '0', null, '1', '0', '2018-03-14 14:03:01', '2018-03-14 14:03:01');
INSERT INTO `ams_api` VALUES ('34', 'baidu111', 'www.163.com', 'HTTP', 'POST', 'formData', '', null, null, '0', null, '1', '0', '2018-03-14 14:05:21', '2018-03-14 14:05:21');
INSERT INTO `ams_api` VALUES ('35', 'baidu111', 'www.163.com', 'HTTP', 'POST', 'formData', '', null, null, '0', null, '2', '0', '2018-03-14 14:06:44', '2018-03-14 14:06:44');
INSERT INTO `ams_api` VALUES ('36', 'baidu111222', 'www.163.com', 'HTTP', 'POST', 'formData', '', null, null, '0', null, '2', '0', '2018-03-14 14:13:11', '2018-03-14 14:13:11');
INSERT INTO `ams_api` VALUES ('38', '阳光易购', 'www.ebid360.com', 'HTTP', 'POST', 'raw', 0x61616161616161616161616262626262626262626262626262626262626262626262, 0x616161616161616161616161, 0x7BE28098636F6465E280993A313131317D, '0', null, '2', '5', '2018-03-21 15:19:41', '2018-03-21 15:19:41');
INSERT INTO `ams_api` VALUES ('39', 'fdsafdsafsadfdsaf', 'fdasfsadfsa', 'HTTP', 'POST', 'formData', '', '', '', '0', null, '2', '0', '2018-03-15 09:45:58', '2018-03-15 09:45:58');
INSERT INTO `ams_api` VALUES ('40', 'aa', 'aa', 'HTTP', 'POST', 'formData', '', '', '', '0', null, '2', '3', '2018-03-16 14:16:32', '2018-03-16 14:16:32');
INSERT INTO `ams_api` VALUES ('42', '加法接口测试', '127.0.0.1:8000/test/add/', 'HTTP', 'POST', 'formData', '', 0x33, '', '0', null, '2', '4', '2018-03-16 15:45:53', '2018-03-16 15:45:53');
INSERT INTO `ams_api` VALUES ('43', 'aaa', 'aaa', 'HTTP', 'POST', 'formData', '', '', '', '0', '2', '1', '5', '2018-03-21 22:33:41', '2018-03-21 22:33:41');

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
INSERT INTO `ams_api_group` VALUES ('1', '教师管理列表', '1');
INSERT INTO `ams_api_group` VALUES ('2', '登录模块', '1');

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
INSERT INTO `ams_api_header` VALUES ('21', 'a', 'b', '25');
INSERT INTO `ams_api_header` VALUES ('23', 'a', 'b', '27');
INSERT INTO `ams_api_header` VALUES ('24', 'a', 'b', '28');
INSERT INTO `ams_api_header` VALUES ('28', 'a', 'b', '32');
INSERT INTO `ams_api_header` VALUES ('30', 'a', 'b', '34');
INSERT INTO `ams_api_header` VALUES ('31', 'a', 'b', '35');
INSERT INTO `ams_api_header` VALUES ('32', 'a', 'b', '36');
INSERT INTO `ams_api_header` VALUES ('36', 'Accept', 'aaa', '39');
INSERT INTO `ams_api_header` VALUES ('37', 'a', 'a', '40');
INSERT INTO `ams_api_header` VALUES ('39', 'area', '010', '38');
INSERT INTO `ams_api_header` VALUES ('40', 'uid', '10001', '38');
INSERT INTO `ams_api_header` VALUES ('41', '111', '1222', '43');
INSERT INTO `ams_api_header` VALUES ('42', 'a', 'b', '23');

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
INSERT INTO `ams_api_request_param` VALUES ('31', 'cc', 'dd', '0', '23', '0');

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
INSERT INTO `ams_project` VALUES ('1', '0', '教师管理系统', '2018-03-21 14:29:45', '1.0');
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
INSERT INTO `ams_test_case` VALUES ('1', '1', '登录成功', null, null, null, '2018-03-21 17:16:45', '3', '0', null);
INSERT INTO `ams_test_case` VALUES ('3', '1', 'cccc2222', null, null, null, '2018-03-21 17:23:45', '4', '0', null);
INSERT INTO `ams_test_case` VALUES ('4', '2', 'dddd', null, null, null, '2018-03-20 14:29:45', '1', '0', null);
INSERT INTO `ams_test_case` VALUES ('7', '1', '登录-用户名不存在', null, null, null, '2018-03-21 17:17:08', '3', '0', null);

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
INSERT INTO `ams_test_case_group` VALUES ('3', '教师登录', '1');
INSERT INTO `ams_test_case_group` VALUES ('4', 'aaa', '1');

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
INSERT INTO `ams_test_case_item` VALUES ('6', '1', '{\"headers\": [{\"headerName\": \"a1\", \"headerValue\": \"11\"}, {\"headerName\": \"fffffffff\", \"headerValue\": \"fffffffffff\"}], \"apiUri\": \"fdsfdsaf\", \"apiProtocol\": \"HTTP\", \"apiMethod\": \"POST\", \"requestType\": \"raw\", \"raw\": \"fdsafsafsaffaffffsaf\", \"params\": []}', null, '200', '3', '[{\"paramKey\":\"aaa\",\"matchRule\":\"0\",\"paramInfo\":\"dddd\"},{\"paramKey\":\"cc\",\"matchRule\":\"0\",\"paramInfo\":\"cc\"}]', '获取教师信息', 'fdsfdsaf', 'POST', 'HTTP');
INSERT INTO `ams_test_case_item` VALUES ('7', '7', '{\"headers\": [], \"apiUri\": \"www.aaa.com/login\", \"apiProtocol\": \"HTTP\", \"apiMethod\": \"POST\", \"requestType\": \"formData\", \"params\": [{\"paramName\": \"username\", \"paramValue\": \"1\"}]}', null, '200', '0', '', '登录', 'www.aaa.com/login', 'POST', 'HTTP');

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
