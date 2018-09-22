var test = require('unit.js');
var EntryLogModule = require('../Parse-Log-File/EntryLog');
var parserModule = require('../Parse-Log-File/LogEntryParser');

var log = "00:10:30 00:15:30\n" +
    "00:11:30 00:15:30\n" +
    "00:12:30 00:16:00";
var parser = new parserModule.LogEntryParser();
var entryLog = new EntryLogModule.EntryLog(parser);
var entries = parser.splitEntriesByLine(log);

test.object(entries).isNotEmpty();
test.array(["00:10:30 00:15:30", "00:11:30 00:15:30", "00:12:30 00:16:00"]).is(entries);

var date = parser.getStartDate();
test.value(date.getHours()).is(0);
test.value(date.getMinutes()).is(0);
test.value(date.getSeconds()).is(0);

var entry = parser.parseEntryExit("00:10:30 00:15:30");
test.array(entry).is(["00:10:30", "00:15:30"]);

var timeSplit = parser.parseEntryTime("00:10:30");
test.array(timeSplit).is(["00", "10", "30"]);
timeSplit = parser.parseExitTime("00:10:30");
test.array(timeSplit).is(["00", "10", "30"]);
timeSplit = parser.parseExitTime("");
test.value(timeSplit).is(null);

var end = new Date();
var entryDate = parser.setEntryExitDate(end, 0, 10, 30);
test.value(entryDate.getHours()).is(0);
test.value(entryDate.getMinutes()).is(10);
test.value(entryDate.getSeconds()).is(30);

var diff = parser.getDateDiff(date, end);
test.value(diff).is(10 * 60 + 30);

var entryList = entryLog.parseLog(log);
test.value(entryList[15*60]).is(3);
test.value(entryList[15*60 + 30]).is(1);
test.value(entryList[17*60]).is(0);
