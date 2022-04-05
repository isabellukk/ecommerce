import environ
import stripe


env = environ.Env()
environ.Env.read_env()

let stripe = Stripe(env('STRIPE_SECRET_KEY'))
