<script lang="ts">
	import { sampleClassSchedule } from './data/sampleSchedule';

	const today = new Date();
	const currentYear = today.getFullYear();
	const currentMonth = today.getMonth();

	const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

	const colorMap: Record<string, string> = {
		'6:00AM': 'lightblue',
		'7:00AM': 'lightpink',
		'8:00AM': 'lightgray',
		'12:00PM': 'plum',
		'5:00PM': 'lightyellow',
		'6:30PM': 'lightgreen'
	};

	function generateCalendarGrid(year: number, month: number): (number | null)[] {
		const days: (number | null)[] = [];
		const firstDayIndex = new Date(year, month, 1).getDay();
		const totalDays = new Date(year, month + 1, 0).getDate();

		// add beginning nulls
		for (let i = 0; i < firstDayIndex; i++) {
			days.push(null);
		}

		// add days for the month
		for (let i = 1; i <= totalDays; i++) {
			days.push(i);
		}

		// fill month grid
		while (days.length % 7 !== 0) {
			days.push(null);
		}

		return days;
	}

	const calendarGrid = generateCalendarGrid(currentYear, currentMonth);

	function getShiftsForDay(day: number) {
		const dateStr = `${(currentMonth + 1).toString().padStart(2, '0')}/${day.toString().padStart(2, '0')}/${currentYear}`;
		const daySchedule = sampleClassSchedule.find((schedule) => schedule.date === dateStr);
		return daySchedule ? daySchedule.shifts : [];
	}
</script>

<div class="calendar">
	{#each daysOfWeek as day}
		<div class="days-header">
			{day}
		</div>
	{/each}
	{#each calendarGrid as day}
		<div class="calendar-cell">
			{#if day !== null}
				<div class="day-as-number">{day}</div>
				<div class="shifts-container">
					{#each getShiftsForDay(day) as supportShift}
						<div
							class="shift"
							style="background: {supportShift.supportStaff != ''
								? colorMap[supportShift.time] || 'white'
								: 'red'}"
						>
							{supportShift.time}: {supportShift.supportStaff}
						</div>
					{/each}
				</div>
			{/if}
		</div>
	{/each}
</div>

<style>
	.calendar {
		display: grid;
		grid-template-columns: repeat(7, 1fr);
		width: 100%;
		border: 1px solid black;
	}

	.days-header {
		display: flex;
		justify-content: center;
		font-weight: 700;
		background: var(--light-grey);
		height: fit-content;
		padding: 5px;
		border-bottom: 1px solid black;
	}

	.calendar-cell {
		display: flex;
		flex-direction: column;
		align-items: center;
		padding: 10px;
		border: 1px solid var(--light-grey);
	}

	.day-as-number {
		padding-bottom: 10px;
	}

	.shifts-container {
		display: flex;
		flex-direction: column;
		gap: 4px;
		width: 100%;
		box-sizing: border-box;
	}

	.shift {
		display: flex;
		justify-content: center;
		width: 100%;
		border-radius: 10px;
		font-size: 12px;
		padding: 2px 15px;
		box-sizing: border-box;
	}
</style>
