<script lang="ts">
	let selectedName: string = '';
	let selectedDate: string = '';
	let selectedTime: string = '';

	const staff: string[] = ['Sophie', 'Mihir', 'Erika', 'Crystal', 'Shazi'];
	const classTimes: string[] = ['6:00AM', '7:00AM', '8:00AM', '12:00PM', '5:00PM', '6:30PM'];

	function handleSearch() {
		console.log(
			`${selectedName} is requesting a sub for ${selectedDate} at ${selectedTime}. Are you available?`
		);
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
	<button on:click={handleSearch}> Find a sub </button>
</div>

<style>
	.sub-form {
		display: flex;
		flex-direction: column;
		width: 100%;
		gap: 20px;
	}
	.sub-form form {
		display: flex;
		gap: 20px;
		width: 100%;
	}

	.sub-form form label {
		font-weight: 500;
	}

	.form-item {
		display: flex;
		flex-direction: column;
		gap: 6px;
	}

	button {
		align-self: center;
		width: 40%;
		border: none;
	}
</style>
