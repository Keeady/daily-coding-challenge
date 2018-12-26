function compareVersions(version1, version2) {
    var version1Array = version1.split('.');
    var version2Array = version2.split('.');
    var i = 0, j = 0;
    var v1, v2;
    while (i < version1Array.length || j < version2Array.length) {
        if (i >= version1Array.length) {
            v1 = 0;
        }
        else {
            v1 = parseInt(version1Array[i]);
        }
        if (j >= version2Array.length) {
            v2 = 0;
        }
        else {
            v2 = parseInt(version2Array[j]);
        }
        if (v1 < v2) {
            return -1;
        }
        else if (v1 > v2) {
            return 1;
        }
        i++;
        j++;
    }
    return 0;
}
module.exports = compareVersions;
