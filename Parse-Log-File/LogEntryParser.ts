export class LogEntryParser {
    /**
     * @param {string} log
     * @returns {string[]}
     */
    splitEntriesByLine(log: string) {
        return log.split('\n');
    }

    /**
     * @returns {Date}
     */
    getStartDate() {
        let startDate = new Date();
        startDate.setHours(0, 0, 0);

        return startDate;
    }

    /**
     * @param {string} entryLog
     * @returns {string[]}
     */
    parseEntryExit(entryLog) {
        return entryLog.split(' ');
    }

    /**
     * @param {string} time
     * @returns {string[]}
     */
    parseEntryTime(time) {
        return time.split(':');
    }

    /**
     * @param {string} time
     * @returns {any}
     */
    parseExitTime(time) {
        if (time) {
            return time.split(':');
        }

        return null;
    }

    /**
     * @param {string} date
     * @param {number} hours
     * @param {number} min
     * @param {number} sec
     * @returns {any}
     */
    setEntryExitDate(date, hours, min, sec) {
        date.setHours(parseInt(hours), parseInt(min), parseInt(sec));

        return date;
    }

    /**
     * @param {Date} start
     * @param {Date} end
     * @returns {number}
     */
    getDateDiff(start: Date, end: Date) {
        return parseInt(Math.abs(start - end) / 1000);
    }
}
