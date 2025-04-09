<script lang="ts">
	// load custom types
	import type { StaffAvailability } from './types/StaffAvailability';

	// load sample data - this should change eventually
	import { sampleData } from './data/sampleData';

	// set dropdown consts - this should become dynamic at some point
	const staff: string[] = ['Sophie', 'Mihir', 'Erika', 'Crystal', 'Shazi'];
	const classTimes: string[] = ['6:00am', '7:00am', '8:00am', '12:00pm', '5:00pm', '6:30pm'];

	// instantiate callback props
	export let availableStaff: (staff: StaffAvailability[]) => void;
	export let setShowSubModal: (value: boolean) => void;
	export let setShowResults: (value: boolean) => void;

	// instantiate vars for form values
	let selectedName: string = '';
	let selectedDate: string = '';
	let selectedTime: string = '';

	// cancel logic
	function handleCancel() {
		setShowSubModal(false);
	}

	// define logic for when a user submits a sub request
	function handleSearch() {
		// parse date to match our sample data
		const dateObj = new Date(selectedDate);
		const dayOfWeek = dateObj.toLocaleDateString('en-US', { weekday: 'long' }).toLowerCase();

		// filter full staff list to those who have availability matching the request
		const filteredStaff = sampleData.filter((person) =>
			person.availability[dayOfWeek as keyof typeof person.availability]?.includes(selectedTime)
		);

		// populate props for callback
		availableStaff(filteredStaff);
		setShowResults(true);
	}
</script>

<div class="sub-form">
	<datalist id="name-options">
		{#each staff as person}
			<option value={person}></option>
		{/each}
	</datalist>
	<datalist id="time-options">
		{#each classTimes as time}
			<option value={time}></option>
		{/each}
	</datalist>
	<form>
		<div class="form-item">
			<label for="options">Your Name:</label>
			<input
				list="name-options"
				id="options"
				name="options"
				placeholder="Select your name..."
				bind:value={selectedName}
			/>
		</div>
		<div class="form-item">
			<label for="fdate">Date:</label>
			<input type="date" id="fdate" name="fdate" bind:value={selectedDate} />
		</div>
		<div class="form-item">
			<label for="options">Class Time</label>
			<input
				list="time-options"
				id="options"
				name="options"
				placeholder="Select class time..."
				bind:value={selectedTime}
			/>
		</div>
	</form>
	<div class="modal-buttons">
		<button class="cancel" on:click={handleCancel}> CANCEL </button>
		<button
			class="find {selectedName != '' && selectedDate != '' && selectedTime != ''
				? ''
				: 'find-disabled'}"
			disabled={selectedName === '' || selectedDate === '' || selectedTime === ''}
			on:click={handleSearch}
		>
			FIND A SUB
		</button>
	</div>
</div>

<style>
	.sub-form {
		display: flex;
		flex-direction: column;
		width: 100%;
		gap: 20px;
	}

	.sub-form form {
		align-self: center;
		display: flex;
		width: 100%;
		gap: 20px;
		width: 100%;
	}

	.sub-form form label {
		font-weight: 500;
		font-size: 14px;
	}

	.sub-form form input {
		font-size: 14px;
	}

	.form-item {
		display: flex;
		flex-direction: column;
		width: 100%;
		gap: 6px;
	}

	.modal-buttons {
		display: flex;
		gap: 20px;
		justify-content: center;
	}

	.find-disabled {
		background: var(--disabled-grey);
		cursor: not-allowed;
	}
	.find-disabled:hover {
		transform: none;
	}
</style>
