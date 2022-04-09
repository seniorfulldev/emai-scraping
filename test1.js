

// import MailConfirm from 'mail-confirm'
const emailExistence = require("email-existence");

const emailValidate = async () => {
    const result = emailExistence.check('sales@linktracker.pro', function(error, response){
        console.log('res: ',response);
    });
//   console.log("result");
//   console.log(result);
};

emailValidate();
