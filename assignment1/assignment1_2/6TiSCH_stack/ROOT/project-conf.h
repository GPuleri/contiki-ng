#ifndef PROJECT_CONF_H_
#define PROJECT_CONF_H_

#define ENERGEST_CONF_ON 1

/* Set to enable TSCH security */
#ifndef WITH_SECURITY
#define WITH_SECURITY 1
#endif /* WITH_SECURITY */

/* USB serial takes space, free more space elsewhere */
#define SICSLOWPAN_CONF_FRAG 0
// default 1280
#define UIP_CONF_BUFFER_SIZE 160

/*******************************************************/
/********************* Enable TSCH *********************/
/*******************************************************/

/* Needed for CC2538 platforms only */
/* For TSCH we have to use the more accurate crystal oscillator
 * by default the RC oscillator is activated */
#define SYS_CTRL_CONF_OSC32K_USE_XTAL 1

/*******************************************************/
/******************* Configure TSCH ********************/
/*******************************************************/

/* Enable Sixtop Implementation */
#define TSCH_CONF_WITH_SIXTOP 1

/* Enable security */
#if WITH_SECURITY
#define LLSEC802154_CONF_ENABLED 1
#endif /* WITH_SECURITY */

#endif /* PROJECT_CONF_H_ */
