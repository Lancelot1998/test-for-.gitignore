const Iota = require('@iota/core')

const iota = Iota.composeAPI({
    // replace with your IRI node address 
    // or connect to a Devnet node for testing: 'https://nodes.devnet.iota.org:443'
    provider: 'http://localhost:14265'
})

// Must be truly random & 81-trytes long.
const seed = 'SEED99999999999999999999999999999999999999999999999999999999999999999999999999999'

// Array of transfers which defines transfer recipients and value transferred in IOTAs.
const transfers = [{
    address: 'FJKKSHBZTAKQNDTIKJYCZBOZDGSZANCZSWCNWUOCZXFADNOQSYAHEJPXRLOVPNOQFQXXGEGVDGICLMOXX',
    value: 5, // 1Ki
    tag: '', // optional tag of `0-27` trytes
    message: '' // optional message in trytes
}]

const inputs = [{ 
    address: 'UZXHFCDGGGLTJEJKMNBHZMDOGFHNSGSVRLMYGFOGENGZYUKAR9EHFBISWMLBIOKAFBMLNR99OIEI9J9KW',
    keyIndex: 5,
    security: 2,
    balance: 2779530283277736 
}]

// Depth or how far to go for tip selection entry point.
const depth = 3 
// const minWeightMagnitude = 9
const security = 2
// Difficulty of Proof-of-Work required to attach transaction to tangle.
// Minimum value on mainnet is `14`, `7` on spamnet and `9` on devnet and other testnets

// Prepare a bundle and signs it.
var timestamp = (new Date()).valueOf();
iota.prepareTransfers(seed, transfers, inputs, security)
    .then(trytes => {
        console.log((new Date()).valueOf() - timestamp)
        // Persist trytes locally before sending to network.
        // This allows for reattachments and prevents key reuse if trytes can't
        // be recovered by querying the network after broadcasting.

        // Does tip selection, attaches to tangle by doing PoW and broadcasts.
        //console.log(`ok2`)
        // return iota.sendTrytes(trytes, depth, minWeightMagnitude)
    })
    // .then(bundle => {
    //    console.log(`Published transaction with tail hash: ${bundle[0].hash}`)
    //    console.log(`Bundle: ${JSON.stringify(bundle, null, 1)}`)
    //})
