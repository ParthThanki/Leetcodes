/**
 * @param {number[]} students
 * @param {number[]} sandwiches
 * @return {number}
 */
var countStudents = function(students, sandwiches) {

    let count = 0;

    while(count < students.length && !!students.length) {

        if(students[0] === sandwiches[0]) {
            count = 0;
            students.shift();
            sandwiches.shift();
        } else {
            count += 1;
            let val = students.shift();
            students.push(val);
        }
    }

    return count;
};