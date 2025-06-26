const fs = require('fs');
const s = fs.readFileSync(0, 'utf-8').trim();

if (s === '0') {
  console.log('0');
} else {
  const m = {
    '0': '000', '1': '001', '2': '010', '3': '011',
    '4': '100', '5': '101', '6': '110', '7': '111'
  };
  let r = parseInt(s[0], 8).toString(2);
  for (let i = 1; i < s.length; i++) {
    r += m[s[i]];
  }
  console.log(r);
}