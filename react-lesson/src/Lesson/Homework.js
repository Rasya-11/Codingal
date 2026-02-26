function CustomerDetails() {
  const customer = {
    name: "John Williams",
    email: "john.Williams@email.com",
    age: 32,
    country: "UK",
    balance: 2500 * 2
  };

  const table = (
    <table border="1" cellPadding="10">
      <thead>
        <tr>
          <th>Field</th>
          <th>Details</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>Name</td>
          <td>{customer.name}</td>
        </tr>
        <tr>
          <td>Email</td>
          <td>{customer.email}</td>
        </tr>
        <tr>
          <td>Age</td>
          <td>{customer.age}</td>
        </tr>
        <tr>
          <td>Country</td>
          <td>{customer.country}</td>
        </tr>
        <tr>
          <td>Balance</td>
          <td>£{customer.balance}</td>
        </tr>
      </tbody>
    </table>
  );

  return table;
}

export default CustomerDetails;