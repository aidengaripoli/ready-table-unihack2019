const stripe = require('stripe')('sk_test_8PDtIFKEY5Rj8Pt3y0xhhDjT')

exports.checkout = (req, res) => {
  const { stripeEmail, stripeToken, stripeAmount } = req.body
  console.log(stripeEmail, stripeToken, stripeAmount)

  if (stripeEmail && stripeToken && stripeAmount) {
    console.log('data recieved.')
    stripe.customers
      .create({
        email: stripeEmail,
        source: stripeToken
      })
      .then(customer => {
        console.log('starting the stripe charges')
        stripe.charges.create({
          amount: stripeAmount,
          description: 'Order',
          currency: 'aud',
          customer: customer.id
        })
      })
      .then(charge => {
        console.log('finished the stripe charges')
        res.status(200).json({ message: 'Payment Completed.' })
      })
      .catch(err => {
        console.log(err)
        res.status(500).json({ message: err })
      })
    } else {
      console.error('Missing Stripe Fields.')
      res.status(500).json({ message: 'Missing Stripe Fields.' })
    }
}

