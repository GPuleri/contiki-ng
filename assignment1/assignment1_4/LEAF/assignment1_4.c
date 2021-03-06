#include <stdio.h>
#include "contiki.h"
#include "sys/energest.h"
#include "net/mac/tsch/tsch.h"
#include "net/netstack.h"
#include "net/nullnet/nullnet.h"
#include "sys/stimer.h"
#include "tsch.h"
#include <string.h>
#include "sys/log.h"
#include <time.h>
#include "sys/rtimer.h"

#define LOG_MODULE "App"
#define LOG_LEVEL LOG_LEVEL_INFO

static linkaddr_t root = {{ 0x00, 0x12, 0x4b, 0x00, 0x19, 0x32, 0xe3, 0x0b }};

PROCESS(project1_4, "project1_4");
AUTOSTART_PROCESSES(&project1_4);
/*---------------------------------------------------------------------------*/
static inline unsigned long
to_seconds(uint64_t time) {
   return (unsigned long)(time / ENERGEST_SECOND);
}
/*---------------------------------------------------------------------------*/
void input_callback(const void * data, uint16_t len,
   const linkaddr_t * src, const linkaddr_t * dest) {}

/*---------------------------------------------------------------------------*/
/*
 * This Process will periodically print energest values for the last minute.
 *
 */
PROCESS_THREAD(project1_4, ev, data) {
   static struct etimer periodic_timer;
   static struct stimer eval_timer;
   static bool start = true;
   tsch_schedule_add_link(tsch_schedule_get_slotframe_by_handle(0), LINK_OPTION_TX, 1, &root, 1, 0);

   PROCESS_BEGIN();

   /* Initialize NullNet */
   uint64_t generation;
   nullnet_buf = (uint8_t *)&generation;
   nullnet_len = sizeof(generation);
   nullnet_set_input_callback(input_callback);

   etimer_set(&periodic_timer, CLOCK_SECOND);
   while (1) {
      PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&periodic_timer));
      etimer_reset(&periodic_timer);

      struct tsch_neighbor *nbr = tsch_queue_get_time_source();
      if (nbr != NULL) {

         if (start) {
            start = false;
            energest_init();
            printf("\nConnection established, start the timer for 100 sec..\n");
            stimer_set(&eval_timer, 100); // start the timer.
            tsch_schedule_remove_link_by_timeslot(tsch_schedule_get_slotframe_by_handle(0), 0);
         }

         if (nbr != NULL) {
            generation = tsch_get_network_uptime_ticks(); // get the current timestamp
            LOG_INFO("Sending to ");
            LOG_INFO_LLADDR(&root);
            LOG_INFO_("\n");

            NETSTACK_NETWORK.output(&root); // send packet
         }

         if (!start && stimer_expired(&eval_timer)) {

            /*
             * Update all energest times. Should always be called before energest
             * times are read.
             */
            energest_flush();

            printf("\nEnergest:\n");
            printf(" CPU          %4lus LPM      %4lus DEEP LPM %4lus  Total time %lus\n",
               to_seconds(energest_type_time(ENERGEST_TYPE_CPU)),
               to_seconds(energest_type_time(ENERGEST_TYPE_LPM)),
               to_seconds(energest_type_time(ENERGEST_TYPE_DEEP_LPM)),
               to_seconds(ENERGEST_GET_TOTAL_TIME()));
            printf(" Radio LISTEN %4lus TRANSMIT %4lus OFF      %4lus\n",
               to_seconds(energest_type_time(ENERGEST_TYPE_LISTEN)),
               to_seconds(energest_type_time(ENERGEST_TYPE_TRANSMIT)),
               to_seconds(ENERGEST_GET_TOTAL_TIME() -
                  energest_type_time(ENERGEST_TYPE_TRANSMIT) -
                  energest_type_time(ENERGEST_TYPE_LISTEN)));

            printf("\nEnd of program\n");
            break;
         }

      }
   }
   PROCESS_END();
}
/*---------------------------------------------------------------------------*/
