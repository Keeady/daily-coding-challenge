var test = require('unit.js');
var meetingScheduler = require('../Array/meetingScheduler');
var scheduler = new meetingScheduler.MeetingScheduler(830, 1730);
//end
var result = scheduler.updateAvailableSlot([[[1000, 1100], [1130, 1200]], [[1400,1700]]], 0, 1200, 1330);
var update = [[[1000, 1100], [1130, 1200], [1200,1330]], [[1400,1700]]];
test.object(result).is(update);

//beginning
result = scheduler.updateAvailableSlot([[[1000, 1100], [1130, 1200]], [[1400,1700]]], 0, 900, 945);
update = [[[900, 945], [1000, 1100], [1130, 1200]], [[1400,1700]]];
test.object(result).is(update);

//middle
result = scheduler.updateAvailableSlot([[[1000, 1100], [1130, 1200]], [[1400,1700]]], 0, 1100, 1130);
update = [[[1000, 1100],[1100,1130], [1130, 1200]], [[1400,1700]]];
test.object(result).is(update);

//no update
result = scheduler.updateAvailableSlot([[[1000, 1100], [1130, 1200]], [[1400,1700]]], 1, 1100, 1500);
update = [[[1000, 1100], [1130, 1200]], [[1400,1700]]];
test.object(result).is(update);

result = scheduler.updateAvailableSlot([[[1000, 1100], [1130, 1200]], [[1400,1700]]], 1, 1100, 1400);
update = [[[1000, 1100], [1130, 1200]], [[1100, 1400], [1400,1700]]];
test.object(result).is(update);

result = scheduler.updateAvailableSlot([[[1000, 1100], [1130, 1200]], [[1400,1700]]], 1, 630, 1400);
update = [[[1000, 1100], [1130, 1200]], [[1400,1700]]];
test.object(result).is(update);

result = scheduler.updateAvailableSlot([[[1000, 1100], [1130, 1200]], [[1400,1700]]], 3, 1000, 1400);
update = [[[1000, 1100], [1130, 1200]], [[1400,1700]]];
test.object(result).is(update);
