<script lang="ts">
	// import custom types
	import type { StaffAvailability } from './types/Staff';

	// import child components
	import SubForm from './SubForm.svelte';

	// set prop for callback
	export let setShowSubModal: (value: boolean) => void;

	// instanatite vars for component
	let availableStaff: StaffAvailability[] = [];
	let showResults: boolean = false;
	let headerText: string = "Let's get the details";

	// handle callbacks
	function handleFoundStaff(staff: StaffAvailability[]) {
		availableStaff = staff;
	}
	function handleSetShowResults(value: boolean) {
		showResults = value;
		headerText = "Here's who's available";
	}

	// logic to actually request the sub (for now just a console log)
	function handleSubOptionClick(subName: string) {
		console.log('Requesting Sub From: ', subName);
	}
</script>

<div class="sub-modal">
	<h4>{headerText}</h4>
	<div class="modal-contents">
		<div class="form-container" style={showResults ? 'display: none' : 'display: flex'}>
			<SubForm
				availableStaff={handleFoundStaff}
				{setShowSubModal}
				setShowResults={handleSetShowResults}
			/>
		</div>
		<div class="results" style={showResults ? 'display: flex' : 'display: none'}>
			<div class="available-staff">
				{#each availableStaff as subOption}
					<button
						class="staff-member"
						on:click={() => console.log(`Requesting a sub from ${subOption.firstName}`)}
					>
						{subOption.firstName}
						{subOption.lastName}
					</button>
				{/each}
			</div>
			<button on:click={() => handleSetShowResults(false)}>BACK</button>
		</div>
	</div>
</div>

<style>
	.sub-modal {
		display: flex;
		flex-direction: column;
		width: 100%;
		border: 1px solid black;
	}

	.sub-modal h4 {
		background: var(--primary-blue);
		color: white;
		margin: 0;
		padding: 20px;
	}

	.modal-contents {
		display: flex;
		padding: 20px;
	}

	.results {
		display: flex;
		flex-direction: column;
		align-content: flex-start;
		width: 100%;
		gap: 20px;
	}

	.available-staff {
		display: flex;
		flex-direction: column;
		font-size: 14px;
		gap: 5px;
	}

	.staff-member {
		display: flex;
		padding: 10px;
		border-radius: 2px;
		width: 100%;
		color: black;
		background: transparent;
	}

	.staff-member:hover {
		background: rgb(241, 241, 241);
		display: flex;
		padding: 10px;
		border-radius: 2px;
		width: 100%;
	}

	button {
		background: black;
		color: white;
		align-self: center;
		width: 100px;
		border: none;
		padding: 10px;
		border-radius: 2px;
		transition:
			transform 0.2s ease-out,
			box-shadow 0.2s ease-out;
		font-size: 12px;
	}

	button:hover {
		transform: translateY(-0.125rem);
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	}
</style>
