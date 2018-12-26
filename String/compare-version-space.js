function compareVersionSpace(version1, version2) {
    var i = 0, j = 0;
    var v1, v2;
    var subLength;
    //10.6.5
    //10.6
    while (i < version1.length || j < version2.length) {
        subLength = getVersion(version1, i, 1);
        v1 = subLength ? parseInt(version1.substr(i, subLength)) : 0;
        i += subLength + 1;
        subLength = getVersion(version2, j, 1);
        v2 = subLength ? parseInt(version2.substr(j, subLength)) : 0;
        j += subLength + 1;
        if (v1 < v2) {
            return -1;
        }
        else if (v1 > v2) {
            return 1;
        }
    }
    return 0;
}
function getVersion(version, i, j) {
    if (i >= version.length) {
        return 0;
    }
    while (i + j < version.length && version.charAt(i + j) != '.') {
        j++;
    }
    return j;
}
module.exports = compareVersionSpace;
