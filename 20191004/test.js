const korail = require('korail')
const stationStream = korail.stations.all()
 
const seoul = '0001' // station id
const busan = { // FPTF station
    type: 'station',
    id: '0020'
    // …
}
korail.journeys(seoul, busan, { when: new Date('2019-06-27T05:00:00+0200'), product: 'KTX', transfers: 0 }).then(…)