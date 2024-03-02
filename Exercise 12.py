att = int(input("Enter number of attempts: "))
comp = int(input("Enter number of completions: "))
yds = int(input("Enter total passing yards: "))
td = int(input("Enter number of touchdown passes: "))
intercept = int(input("Enter number of interceptions: "))

def passer_rating(att, comp, yds, td, intercept):
    a = (comp / att - 0.3) * 5
    b = (yds / att - 3) * 0.25
    c = (td / att) * 20
    d = (2.375 - (intercept / att * 25))

    rating = (a + b + c + d) / 6 * 100
    return (rating)

rating = passer_rating(att, comp, yds, td, intercept)
print("Passer rating: {:.2f}".format(rating))
