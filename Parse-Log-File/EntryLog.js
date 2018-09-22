"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var EntryLog = /** @class */ (function () {
    /**
     * @param {LogEntryParser} parser
     */
    function EntryLog(parser) {
        this.parser = parser;
    }
    /**
     * @param {string} log
     * @returns {number[]}
     */
    EntryLog.prototype.parseLog = function (log) {
        var logEntries = [];
        var entries = this.parser.splitEntriesByLine(log);
        var i = 0;
        var startDate = this.parser.getStartDate();
        var entryDate = new Date();
        var exitDate = new Date();
        while (i < entries.length) {
            var entryTimes = this.parser.parseEntryExit(entries[i]);
            var entry = this.parser.parseEntryTime(entryTimes[0]);
            var exit = this.parser.parseExitTime(entryTimes[1]);
            entryDate = this.parser.setEntryExitDate(entryDate, entry[0], entry[1], entry[2]);
            var diff = this.parser.getDateDiff(startDate, entryDate);
            if (!logEntries[diff]) {
                logEntries[diff] = 0;
            }
            logEntries[diff] += 1;
            if (exit) {
                exitDate = this.parser.setEntryExitDate(exitDate, exit[0], exit[1], exit[2]);
                diff = this.parser.getDateDiff(startDate, exitDate);
                if (!logEntries[diff]) {
                    logEntries[diff] = 0;
                }
                logEntries[diff] -= 1;
            }
            i++;
        }
        i = 0;
        var value = 0;
        var occupantCount = 0;
        while (i < 84600) {
            value = logEntries[i] || 0;
            occupantCount += value;
            if (occupantCount < 0) {
                occupantCount = 0;
            }
            logEntries[i] = occupantCount;
            i++;
        }
        return logEntries;
    };
    return EntryLog;
}());
exports.EntryLog = EntryLog;
