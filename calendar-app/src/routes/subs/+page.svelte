<script lang="ts">
	import SubModal from '$lib/SubModal.svelte';

	let showModal: boolean = false;
</script>

<main>
	Need a sub?
	<div class="search-modal" style={showModal ? 'display: flex;' : 'display: none;'}>
		<SubModal />
	</div>
</main>

<style>
</style>
