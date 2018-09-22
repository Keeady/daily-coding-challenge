import {LogEntryParser} from "./LogEntryParser";

export class EntryLog {
    protected parser;

    /**
     * @param {LogEntryParser} parser
     */
    constructor(parser: LogEntryParser) {
        this.parser = parser;
    }

    /**
     * @param {string} log
     * @returns {number[]}
     */
    parseLog(log: string) {
        let logEntries = [];
        let entries = this.parser.splitEntriesByLine(log);
        let i = 0;
        let startDate = this.parser.getStartDate();
        let entryDate = new Date();
        let exitDate = new Date();

        while(i < entries.length) {
            let entryTimes = this.parser.parseEntryExit(entries[i]);
            let entry = this.parser.parseEntryTime(entryTimes[0]);
            let exit = this.parser.parseExitTime(entryTimes[1]);

            entryDate = this.parser.setEntryExitDate(entryDate, entry[0], entry[1], entry[2]);
            let diff = this.parser.getDateDiff(startDate, entryDate);
            if (!logEntries[diff]) {
                logEntries[diff] = 0;
            }

            logEntries[diff] +=1;
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
        let value = 0;
        let occupantCount = 0;
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
    }
}
