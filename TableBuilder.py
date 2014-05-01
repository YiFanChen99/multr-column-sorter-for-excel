# -*- coding:utf-8 -*-

__author__ = 'pig'


def _create_table():
    table = [['T', 'T', '', 'org.apache.tools.ant.AntClassLoader', '1026', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.AntClassLoader', '1027', 'T'],
             ['T', '', '', 'org.apache.tools.ant.ComponentHelper', '977', 'T'],
             ['CT', '', '', 'org.apache.tools.ant.Diagnostics', '462', 'T'],
             ['CT', '', '', 'org.apache.tools.ant.Diagnostics', '500', 'T'],
             ['CT', '', '', 'org.apache.tools.ant.Diagnostics', '506', 'T'],
             ['CT', '', '', 'org.apache.tools.ant.Diagnostics', '517', 'T'],
             ['CF', '', '', 'org.apache.tools.ant.Diagnostics', '620', ''],
             ['CF', '', '', 'org.apache.tools.ant.Diagnostics', '621', ''],
             ['T', '', '', 'org.apache.tools.ant.Diagnostics', '505', 'T'],
             ['T', '', '', 'org.apache.tools.ant.Diagnostics', '507', 'T'],
             ['T', '', '', 'org.apache.tools.ant.Diagnostics', '364', 'T'],
             ['T', '', '', 'org.apache.tools.ant.Diagnostics', '624', 'T'],
             ['T', '', '', 'org.apache.tools.ant.Diagnostics', '463', 'T'],
             ['T', '', '', 'org.apache.tools.ant.Diagnostics', '464', 'T'],
             ['T', '', '', 'org.apache.tools.ant.Diagnostics', '501', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.DirectoryScanner', '1244', 'T'],
             ['CT', 'T', '', 'org.apache.tools.ant.filters.ReplaceTokens', '255', 'T'],
             ['', 'T', '', 'org.apache.tools.ant.launch.Launcher', '112', ''],
             ['', '', '', 'org.apache.tools.ant.launch.Launcher', '115', ''],
             ['T', '', '', 'org.apache.tools.ant.launch.Launcher', '293', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.launch.Launcher', '282', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.launch.Launcher', '285', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.launch.Launcher', '289', 'T'],
             ['T', '', '', 'org.apache.tools.ant.listener.CommonsLoggingListener', '92', 'T'],
             ['CT', 'T', '', 'org.apache.tools.ant.listener.MailLogger', '166', 'T'],
             ['CT', 'T', '', 'org.apache.tools.ant.Main', '623', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.Main', '230', 'T'],
             ['CT', 'T', '', 'org.apache.tools.ant.Project', '868', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.ProjectHelperRepository', '107', 'T'],
             ['T', '', '', 'org.apache.tools.ant.ProjectHelperRepository', '112', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.ProjectHelperRepository', '204', 'T'],
             ['T', '', '', 'org.apache.tools.ant.ProjectHelperRepository', '207', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.ProjectHelperRepository', '174', 'T'],
             ['T', '', '', 'org.apache.tools.ant.ProjectHelperRepository', '179', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.Classloader', '241', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.Execute', '219', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.Execute', '170', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.KeySubset', '82', 'T'],
             ['', 'T', '', 'org.apache.tools.ant.taskdefs.KeySubst', '155', ''],
             ['', 'T', '', 'org.apache.tools.ant.taskdefs.optional.ejb.IPlanetEjbc', '307', ''],
             ['', 'T', '', 'org.apache.tools.ant.taskdefs.optional.ejb.IPlanetEjbc', '308', ''],
             ['', 'T', '', 'org.apache.tools.ant.taskdefs.optional.ejb.IPlanetEjbc', '323', ''],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.optional.ejb.IPlanetEjbc', '1482', 'T'],
             ['', 'T', '', 'org.apache.tools.ant.taskdefs.optional.ejb.IPlanetEjbc', '327', ''],
             ['', 'T', '', 'org.apache.tools.ant.taskdefs.optional.ejb.IPlanetEjbc', '331', ''],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.optional.ejb.IPlanetEjbc', '442', 'T'],
             ['', 'T', '', 'org.apache.tools.ant.taskdefs.optional.jlink.jlink', '211', ''],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.optional.junit.FailureRecorder', '263', 'T'],
             ['T', '', '', 'org.apache.tools.ant.taskdefs.optional.junit.JUnitTask', '1078', 'T'],
             ['', 'T', '', 'org.apache.tools.ant.taskdefs.optional.junit.JUnitTestRunner', '810', ''],
             ['', 'T', '', 'org.apache.tools.ant.taskdefs.optional.junit.JUnitTestRunner', '906', ''],
             ['', 'T', '', 'org.apache.tools.ant.taskdefs.optional.junit.JUnitTestRunner', '826', ''],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.optional.junit.TearDownOnVmCrash', '134', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.optional.junit.TearDownOnVmCrash', '137', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.optional.PropertyFile', '386', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.optional.sound.AntSoundPlayer', '110', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.optional.sound.AntSoundPlayer', '125', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.optional.TraXLiaison', '350', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.optional.TraXLiaison', '409', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.ProcessDestroyer', '103', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.ProcessDestroyer', '110', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.ProcessDestroyer', '132', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.ProcessDestroyer', '139', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.ProcessDestroyer', '87', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.Property', '576', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.Property', '572', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.taskdefs.XSLTProcess', '928', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.types.selectors.modifiedselector.PropertiesfileCache', '140', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.types.selectors.modifiedselector.PropertiesfileCache', '167', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.types.selectors.TokenizedPath', '154', 'T'],
             ['T', 'T', '', 'org.apache.tools.ant.util.LayoutPreservingProperties', '700', 'T']]
    return table


def _assert_same_length(table):
    comment_length = len(table[0])
    for row in table:
        if len(row) != comment_length:
            raise Exception('Illegal arguments!')


def build_table():
    table = _create_table()
    _assert_same_length(table)
    return table
