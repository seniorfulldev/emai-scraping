module.exports = {
  

    groupByName: function (original) {
        var uniqueEmails = [];
        original.forEach(function (value) {
            if (uniqueEmails.indexOf(value) === -1) {
                uniqueEmails.push(value);
            }
        });
        return uniqueEmails;
    }
};