export class MeetingScheduler {
    protected startTime: number;
    protected endTime: number;

    /**
     * @param {number} startTime
     * @param {number} endTime
     */
    constructor(startTime: number, endTime: number) {
        this.startTime = startTime;
        this.endTime = endTime;
    }

    /**
     * @param {number[][]} schedule
     * @param {number} room
     * @param {number} start
     * @param {number} end
     * @returns {number[][]}
     */
    updateAvailableSlot(schedule: number[][], room: number, start: number, end: number) {
        if (room >= schedule.length) {
            return schedule;
        }

        let roomSchedule = schedule[room];
        let slot;
        let index;
        let slotEndTime, slotStartTime;
        let isUpdated = false;

        if (this.isValidSlot(start, end, this.startTime, this.endTime) === false) {
            return schedule;
        }

        slotStartTime = this.startTime;
        for (index = 0; index < roomSchedule.length; index++) {
            slot = roomSchedule[index];
            slotEndTime = slot[0];
            if (this.isValidSlot(start, end, slotStartTime, slotEndTime)) {
                let newSlot = [start, end];
                roomSchedule.splice(index, 0, newSlot);
                schedule[room] = roomSchedule;
                isUpdated = true;
                break;
            }

            slotStartTime = slot[1];
        }

        if (isUpdated === false) {
            slotEndTime = this.endTime;
            if (this.isValidSlot(start, end, slotStartTime, slotEndTime)) {
                let newSlot = [start, end];
                roomSchedule.splice(index, 0, newSlot);
                schedule[room] = roomSchedule;
            }
        }

        return schedule;
    }

    /**
     * @param {number[][]} schedule
     * @param {number} meetingLength
     * @returns {any}
     */
    findAvailableSlot(schedule: number[][], meetingLength: number) {
        let index;
        let roomIndex;
        let roomSchedule;
        let previousStart;
        let duration;
        let availableSlot = {};
        let slotIndex;

        if (schedule.length == 0) {
            availableSlot = {
                room: 0,
                startTime: this.startTime,
                endTime: this.startTime + meetingLength
            }

            return availableSlot;
        }

        for (roomIndex = 0; roomIndex < schedule.length; roomIndex++) {
            roomSchedule = schedule[roomIndex];
            previousStart = this.startTime;

            for (slotIndex = 0; slotIndex < roomSchedule.length; slotIndex++) {
                duration = roomSchedule[slotIndex][0] - previousStart;
                if (duration >= meetingLength) {
                    availableSlot = {
                        room: roomIndex,
                        startTime: previousStart,
                        endTime: previousStart + meetingLength
                    };
                    return availableSlot;
                }
                previousStart = roomSchedule[slotIndex][1];
            }
            duration = this.endTime - previousStart;
            if (duration >= meetingLength) {
                availableSlot = {
                    room: roomIndex,
                    startTime: previousStart,
                    endTime: previousStart + meetingLength
                };
                return availableSlot;
            }
        }

        return [];
    }

    /**
     * @param start
     * @param end
     * @param slotStartTime
     * @param slotEndTime
     * @returns {boolean}
     */
    protected isValidSlot(start, end, slotStartTime, slotEndTime) {
        const duration = end - start;
        return slotEndTime - slotStartTime >= duration && start >= slotStartTime && start < slotEndTime && end > slotStartTime && end <= slotEndTime;
    }
}
