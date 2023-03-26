const motelCustomer = {
    firstName: "Albert",
    lastName: "Perfosi",
    birthYear: "1997",
    gender: "Male",
    roomPreferences: ["Mini-bar", "View on ocean", "2 Queen-size beds"],
    paymentMethod: "Debit card",
    mailAddress: {
        street: "36 Aquastreet",
        city: "St.John's",
        province: "NL",
        postalCode: "A3R5E7",
    },
    phoneNumber: "709-325-5432",
    checkIn: {
        date: "2023-03-21",
        time: "11:00",
    },
    checkOut: {
        date: "2023-03-29",
        time: "18:00",
    },
    getAge: function() {
        const today =  new Date();
        return today.getFullYear() - this.birthYear;
    },
    getDurationOfStay: function() {
        const checkIn = new Date(`${this.checkIn.date}`);
        const checkOut = new Date(`${this.checkOut.date}`);
        const oneDay = 1000 * 60 * 60 * 24;
        const diffMil = checkOut.getTime() - checkIn.getTime();
        const durationOfStay = Math.round(diffMil / oneDay);
        return durationOfStay
    }
};

const html = `
    <h1>Customer Info</h1>
    <ul>
    <p>Name: ${motelCustomer.firstName} ${motelCustomer.lastName}</p>
    <p>Age: ${motelCustomer.getAge()}</p>
    <p>Gender: ${motelCustomer.gender}</p>
    <p>Room preferences: ${motelCustomer.roomPreferences.join(", ")}</p>
    <p>Payment method: ${motelCustomer.paymentMethod}</p>
    <p>Mailing Address: ${motelCustomer.mailAddress.street}, ${motelCustomer.mailAddress.city}, ${motelCustomer.mailAddress.province}, ${motelCustomer.mailAddress.postalCode}</p>
    <p>Phone number: ${motelCustomer.phoneNumber}</p>
    <p>Check-In date: ${motelCustomer.checkIn.date}</p>
    <p>Check-In time: ${motelCustomer.checkIn.time}</p>
    <p>Check-Out date: ${motelCustomer.checkOut.date}</p>
    <p>Check-Out time: ${motelCustomer.checkOut.time}</p>
    <p>Duration of Stay: ${motelCustomer.getDurationOfStay()} day(s)</p>
    </ul>
`;

console.log(html);
document.body.innerHTML = html;
