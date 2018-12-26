var test = require('unit.js');
var meetingScheduler = require('../Array/meetingScheduler');
var scheduler = new meetingScheduler.MeetingScheduler(930, 1730);
var result = scheduler.findAvailableSlot([[[1000, 1100], [1130, 1200]], [[1400,1700]]], 130);
test.object(result).is({room: 0, startTime: 1200, endTime: 1330});

result = scheduler.findAvailableSlot([[[1000, 1100], [1130, 1200], [1230,1700]], [[1400,1700]]], 100);
test.object(result).is({room: 1, startTime: 930, endTime: 1030});

result = scheduler.findAvailableSlot([[[1000, 1100], [1130, 1200], [1600,1700]], [[1400,1700]]], 300);
test.object(result).is({room: 0, startTime: 1200, endTime: 1500});

result = scheduler.findAvailableSlot([[[930, 1230], [1130, 1200], [1600,1700]], [[1400,1700]]], 30);
test.object(result).is({room: 0, startTime: 1200, endTime: 1230});

