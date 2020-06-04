const Iota = require('@iota/core')

const iota = Iota.composeAPI({
    // replace with your IRI node address 
    // or connect to a Devnet node for testing: 'https://nodes.devnet.iota.org:443'
    provider: 'http://localhost:14265'
})
seed = 'SEED99999999999999999999999999999999999999999999999999999999999999999999999999999'

a = iota.getInputs(seed, { start: 0 })
  .then(({ inputs, totalBalance }) => {
     console.log(inputs)
  })
  .catch(err => {
    if (err.message === errors.INSUFFICIENT_BALANCE) {
       // ...
    }
    // ...
  })

