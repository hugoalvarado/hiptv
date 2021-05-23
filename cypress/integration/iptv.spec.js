describe('IPTV-Grab-Token', () => {
    Cypress.on('uncaught:exception', (err, runnable) => {
        // returning false here prevents Cypress from
        // failing the test
        return false
      })

    it('Grabs token', () => {
        cy.intercept('POST', '/data.php').as('data')
        cy.visit('https://ustvgo.tv/trutv/')
        cy.wait('@data', { timeout: 400000 }).then((resp) => {
            const token = resp.response.body.split('wmsAuthSign=')[1]
            cy.writeFile('ustvgotoken.js', `var ustvgotoken = "${token}"; `)
        })
    })
  })
