function potionEncoder(potion: string) {
    let potionInput = potion.trim();
    potionInput = potionInput.toUpperCase();
    if (potionInput.length == 0) {
        return potionInput;
    }

    if (potionInput.length == 1) {
        return potionInput;
    }

    let encodedPortion = potionInput[0];

    return encode(potionInput,1, encodedPortion);
}

function encode(potion: string, length: number, encodedPortion: string) {
    if (potion.length <= length) {
        return encodedPortion;
    }

    if (potion.length < length * 2) {
        let i = length;
        while (i < potion.length) {
            encodedPortion += potion.charAt(i);
            i++;
        }

        return encodedPortion;
    }

    if (potion.substring(0, length) == potion.substring(length, length + length)) {
        length += length;
        encodedPortion += '*';
    } else {
        encodedPortion += potion.charAt(length);
        length += 1;
    }

    return encode(potion, length, encodedPortion);
}

module.exports = potionEncoder;
