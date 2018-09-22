"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var LogEntryParser = /** @class */ (function () {
    function LogEntryParser() {
    }
    /**
     * @param {string} log
     * @returns {string[]}
     */
    LogEntryParser.prototype.splitEntriesByLine = function (log) {
        return log.split('\n');
    };
    /**
     * @returns {Date}
     */
    LogEntryParser.prototype.getStartDate = function () {
        var startDate = new Date();
        startDate.setHours(0, 0, 0);
        return startDate;
    };
    /**
     * @param {string} entryLog
     * @returns {string[]}
     */
    LogEntryParser.prototype.parseEntryExit = function (entryLog) {
        return entryLog.split(' ');
    };
    /**
     * @param {string} time
     * @returns {string[]}
     */
    LogEntryParser.prototype.parseEntryTime = function (time) {
        return time.split(':');
    };
    /**
     * @param {string} time
     * @returns {any}
     */
    LogEntryParser.prototype.parseExitTime = function (time) {
        if (time) {
            return time.split(':');
        }
        return null;
    };
    /**
     * @param {string} date
     * @param {number} hours
     * @param {number} min
     * @param {number} sec
     * @returns {any}
     */
    LogEntryParser.prototype.setEntryExitDate = function (date, hours, min, sec) {
        date.setHours(parseInt(hours), parseInt(min), parseInt(sec));
        return date;
    };
    /**
     * @param {Date} start
     * @param {Date} end
     * @returns {number}
     */
    LogEntryParser.prototype.getDateDiff = function (start, end) {
        return parseInt(Math.abs(start - end) / 1000);
    };
    return LogEntryParser;
}());
exports.LogEntryParser = LogEntryParser;
